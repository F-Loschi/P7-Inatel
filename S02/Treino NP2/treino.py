from datetime import datetime

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

import redis
import json

class CassandraDBConnector:
    client_id = "GAekrfAwsPDzdGreXkdLeNpo"
    client_secret = "Z4HzNxUPIrG.1ID14J5I5xkN.bny,rbS2C4pdsf1ZjWGbMQ_JA.+iG,HqxFnbpCFO77ZZMjv3fBuDQlYxYnD,0q_-zE_2ZBdyodtRxICr0qNi6EwYQ3NT.CX-Z8NZtnf"
    cloud_config={ "secure_connect_bundle": "secure-connect-dbiot.zip" }  #TODO use your credentials to connect to cloud provider
    
    nodes = ['localhost']
    port = 9042   

    key_space = "ksiot"  # TODO use your key space
    
    session = None

    @staticmethod
    def get_session():
        if CassandraDBConnector.session == None:
            auth_provider = PlainTextAuthProvider(CassandraDBConnector.client_id, CassandraDBConnector.client_secret)
            cluster = Cluster(cloud=CassandraDBConnector.cloud_config, auth_provider=auth_provider) # TODO use this when using cloud provider
            #cluster = Cluster(
            #    CassandraDBConnector.nodes, 
            #    port=CassandraDBConnector.port
            #) # TODO comment this when using cloud provider
            CassandraDBConnector.session = cluster.connect()
            CassandraDBConnector.session.row_factory = dict_factory
            #CassandraDBConnector.session.execute(""" CREATE KEYSPACE IF NOT EXISTS {} WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': '1' }} """.format(CassandraDBConnector.key_space))  # TODO comment this when using cloud provider
            CassandraDBConnector.session.set_keyspace(CassandraDBConnector.key_space)

            CassandraDBConnector.clean_database() # TODO comment this to keep database

        return CassandraDBConnector.session
    
    @staticmethod
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

    @staticmethod
    def close():
        CassandraDBConnector.session.shutdown()

class RedisDBConnector:

    redis_host = "localhost" #TODO use your credentials to connect
    redis_port = 6379

    connection = None

    @staticmethod
    def get_connection():
        if RedisDBConnector.connection == None:
            #RedisDBConnector.connection = redis.Redis(host=self.redis_host, port=self.redis_port, username=self.redis_username, password=self.redis_password, decode_responses=True)
            RedisDBConnector.connection = redis.Redis(
                host=RedisDBConnector.redis_host, 
                port=RedisDBConnector.redis_port, 
                decode_responses=True
            )
            RedisDBConnector.connection.flushall()
        return RedisDBConnector.connection
    
    @staticmethod
    def close():
        RedisDBConnector.connection.close()

class RestauranteDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        pass

    def adicionar(self, restaurante):
        pass

    def get_restaurantes_cidade(self, cidade: str):
        pass

class PratoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        pass

    def adicionar(self, prato):
        pass

    def get_pratos_restaurante(self, restaurante_id: int):
        pass

class CarrinhoDAO:
    def __init__(self):
        self.redis_connection = RedisDBConnector.get_connection()

    def adicionar_ao_carrinho(self, cliente_id: int, prato_id: int, nome: str, preco: float):
        pass

    def get_carrinho(self, cliente_id: int):
        pass

class PedidoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()
        self.redis_connection = RedisDBConnector.get_connection()

    def criar_tabela(self):
        pass

    def finalizar_pedido(self, id: int, data_hora: datetime, cliente_id: int, restaurante_id: int):
        pass

    def get_pedidos_data(self, data_hora: datetime):
        pass
    