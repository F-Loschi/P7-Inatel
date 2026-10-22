from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

class CassandraDBConnector:
    client_id = "GAekrfAwsPDzdGreXkdLeNpo"
    client_secret = "Z4HzNxUPIrG.1ID14J5I5xkN.bny,rbS2C4pdsf1ZjWGbMQ_JA.+iG,HqxFnbpCFO77ZZMjv3fBuDQlYxYnD,0q_-zE_2ZBdyodtRxICr0qNi6EwYQ3NT.CX-Z8NZtnf"
    cloud_config={ "secure_connect_bundle": "secure-connect-dbiot.zip" }  #TODO use your credentials to connect to cloud provider
    
    nodes = ['localhost']
    port = 9042

    key_space = "ksiot" 
    
    session = None

    staticmethod
    def get_session():
        if CassandraDBConnector.session == None:
            auth_provider = PlainTextAuthProvider(CassandraDBConnector.client_id, CassandraDBConnector.client_secret)
            cluster = Cluster(cloud=CassandraDBConnector.cloud_config, auth_provider=auth_provider) # TODO use this when using cloud provider
            #cluster = Cluster(CassandraDBConnector.nodes, port=CassandraDBConnector.port) # TODO comment this when using cloud provider
            CassandraDBConnector.session = cluster.connect()
            CassandraDBConnector.session.row_factory = dict_factory
            #CassandraDBConnector.session.execute(""" CREATE KEYSPACE IF NOT EXISTS {} WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': '1' }} """.format(CassandraDBConnector.key_space))
            CassandraDBConnector.session.set_keyspace(CassandraDBConnector.key_space)

            CassandraDBConnector.clean_database() # TODO comment this to keep database

        return CassandraDBConnector.session
    
    staticmethod
    def clean_database():
        cassandra_clean_query = f"""
            SELECT table_name FROM system_schema.tables
            WHERE keyspace_name = '{CassandraDBConnector.key_space}';
        """
        tables = CassandraDBConnector.session.execute(cassandra_clean_query)

        # Apagar todas as tabelas do Cassandra
        for table in tables:
             if "table_name" in table.keys():
                table_name = table["table_name"]
                print(f"Apagando tabela: {table_name}")
                CassandraDBConnector.session.execute(f"DROP TABLE IF EXISTS {table_name}")

class CarPart:
    def __init__(self, id, name, car_model, shelf, level, amount):
        self.id = id
        self.name = name
        self.car_model = car_model
        self.shelf = shelf
        self.level = level
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "car_model": self.car_model,
            "shelf": self.shelf,
            "level": self.level,
            "amount": self.amount,
        }

class CarPartDAO:

    def __init__(self) -> None:
        self.cassandra_session = CassandraDBConnector.get_session()

    def create_table(self):
        #---------------------------------------------------------------------Questão 1
        query = 'CREATE TABLE estoque(' \
        'id BIGINT,' \
        'name TEXT,' \
        'car_model TEXT,' \
        'shelf INT,' \
        'level INT,' \
        'amount BIGINT,' \
        'PRIMARY KEY((shelf), car_model, id));'
        self.cassandra_session.execute(query)

    def add_part(self, part : CarPart):
        #---------------------------------------------------------------------Questão 2
        query = 'INSERT INTO estoque(id, name, car_model, shelf, level, amount) VALUES (?, ?, ?, ?, ?, ?);'
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [part.id, part.name, part.car_model, part.shelf, part.level, part.amount])
    
    def get_shelf_parts(self, shelf):
        #---------------------------------------------------------------------Questão 3
        query = 'SELECT name, car_model, amount FROM estoque WHERE shelf = ?;'
        prepared = self.cassandra_session.prepare(query)
        result = self.cassandra_session.execute(prepared, [shelf])
        return list(result)

    def get_car_parts(self, car_model):
        #---------------------------------------------------------------------Questão 4
        query = 'SELECT name, shelf, level, amount FROM estoque WHERE car_model = ? ALLOW FILTERING;'
        prepared = self.cassandra_session.prepare(query)
        result = self.cassandra_session.execute(prepared, [car_model])
        return list(result)

    def get_shelves_stats(self):
        #---------------------------------------------------------------------Questão 5
        query = 'SELECT shelf, MIN(amount) AS min_amount, MAX(amount) AS max_amount, AVG(amount) as average_amount FROM estoque GROUP BY shelf'
        result = self.cassandra_session.execute(query)
        stats = []
        for row in result:
            row['average_amount'] = int(row['average_amount'])
            stats.append(row)
        return stats


part_dao = CarPartDAO()


# Questões 1, 2 e 3
def test_questao_1e2e3():

    parts_data = [
        {"id":4, "name": "Suspensão",  "car_model": "Argo", "shelf": 1, "level": 1, "amount": 3500},
        {"id":3, "name": "Pistão",  "car_model": "Argo", "shelf": 1, "level": 2, "amount": 1500},
        {"id":2, "name": "Suspensão",  "car_model": "Mustang", "shelf": 3, "level": 5, "amount": 200},
        {"id":1, "name": "Correia",  "car_model": "Argo", "shelf": 1, "level": 3, "amount": 2540},
        {"id":6, "name": "Cabo Câmbio", "car_model": "Argo", "shelf": 3, "level": 5, "amount": 1560},
    ]

    shelf = 1

    expected = [
        {"name": "Suspensão",  "car_model": "Argo", "amount": 3500},
        {"name": "Pistão",  "car_model": "Argo", "amount": 1500},
        {"name": "Correia",  "car_model": "Argo", "amount": 2540},
    ]

    part_dao.create_table()

    for part_data in parts_data:
        part = CarPart(part_data['id'], part_data['name'], part_data['car_model'], part_data['shelf'], part_data['level'], part_data['amount'])
        part_dao.add_part(part=part)
    
    output = part_dao.get_shelf_parts(shelf=shelf)
    
    assert sorted(expected, key=lambda d: d['name']) == sorted(output, key=lambda d: d['name'])

# Questão 4
def test_questao_4():

    car_model = "Argo"

    expected = [
        {"name": "Suspensão", "shelf": 1, "level": 1, "amount": 3500},
        {"name": "Pistão", "shelf": 1, "level": 2, "amount": 1500},
        {"name": "Correia", "shelf": 1, "level": 3, "amount": 2540},
        {"name": "Cabo Câmbio", "shelf": 3, "level": 5, "amount": 1560},
    ]

    
    output = part_dao.get_car_parts(car_model=car_model)

    assert sorted(expected, key=lambda d: d['name']) == sorted(output, key=lambda d: d['name'])


# Questão 5
def test_questao_5():
    expected = [
        {"shelf": 1, "min_amount": 1500, "max_amount": 3500, "average_amount": 2513},
        {"shelf": 3, "min_amount": 200, "max_amount": 1560, "average_amount": 880},
    ]
    
    output = part_dao.get_shelves_stats()

    assert sorted(expected, key=lambda d: d['shelf']) == sorted(output, key=lambda d: d['shelf'])