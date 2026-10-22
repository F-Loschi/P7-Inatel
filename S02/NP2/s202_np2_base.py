from datetime import datetime

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

import redis
import json

from s202_np2_models import Usuario, Produto, Venda

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
    
    def close():
        RedisDBConnector.connection.close()
                                
class UsuarioDAO:   

    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()
        self.redis_connection = RedisDBConnector.get_connection()
    
    def criar_tabela(self):
        query = "CREATE TABLE usuario(" \
        "id INT, " \
        "estado TEXT," \
        "cidade TEXT," \
        "endereco TEXT," \
        "nome TEXT," \
        "email TEXT," \
        "interesses LIST<TEXT>," \
        "PRIMARY KEY((estado, cidade), id));"
        self.cassandra_session.execute(query)

    def adicionar(self, usuario : Usuario):
        query = "INSERT INTO usuario(id, estado, cidade, endereco, nome, email, interesses) VALUES (?, ?, ?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [usuario.id, usuario.estado, usuario.cidade, usuario.endereco, usuario.nome, usuario.email, usuario.interesses])

    def get_quantidade_usuarios(self):
        query = "SELECT COUNT(*) FROM usuario;"
        resultado = self.cassandra_session.execute(query)
        return resultado[0]['count']

    def get_usuarios_estado(self, estado : str):
        usuarios = []

        query = "SELECT * FROM usuario WHERE estado = ? ALLOW FILTERING;"
        prepared = self.cassandra_session.prepare(query)
        resultados = self.cassandra_session.execute(prepared, [estado])

        for resultado in resultados:
            usuario = Usuario(
                id=str(resultado['id']),
                estado=resultado['estado'],
                cidade=resultado['cidade'],
                endereco=resultado['endereco'],
                nome=resultado['nome'],
                email=resultado['email'],
                interesses=resultado['interesses']
            )
            usuarios.append(usuario)
        
        return usuarios

    def adicionar_cache(self, usuario : Usuario):
        self.redis_connection.set(f"usuario:{usuario.id}", json.dumps(usuario.to_dict()))
       
    def get_cache(self):
        usuarios = []
        
        chaves = self.redis_connection.keys("usuario:*")
        for chave in chaves:
            usuario_json = self.redis_connection.get(chave)
            usuario_dict = json.loads(usuario_json)
            usuario_cache = Usuario(
                id=usuario_dict['id'],
                estado=usuario_dict['estado'],
                cidade=usuario_dict['cidade'],
                endereco=usuario_dict['endereco'],
                nome=usuario_dict['nome'],
                email=usuario_dict['email'],
                interesses=usuario_dict['interesses']
            )
            usuarios.append(usuario_cache)
        
        return usuarios
        
    def get_interesses_cache(self, usuario_id : int):
        chave = f"usuario:{usuario_id}"
        
        usuario_json = self.redis_connection.get(chave)
        if usuario_json:
            usuario_dict = json.loads(usuario_json)
            return usuario_dict['interesses']
        
        return None

    def adicionar_carrinho_cache(self, usuario_id : int, carrinho : list):
        chave = f"carrinho:{usuario_id}"
        self.redis_connection.set(chave, json.dumps(carrinho))

    def get_carrinho_cache(self, usuario_id : int):
        chave = f"carrinho:{usuario_id}"
        carrinho_json = self.redis_connection.get(chave)
        if carrinho_json:
            return json.loads(carrinho_json)
        return None

class ProdutoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        query = "CREATE TABLE produto(" \
        "id INT," \
        "categoria TEXT," \
        "nome TEXT," \
        "custo FLOAT," \
        "preco FLOAT," \
        "quantidade INT," \
        "PRIMARY KEY ((categoria), id));"
        self.cassandra_session.execute(query)

    def adicionar(self, produto : Produto):
        query = "INSERT INTO produto(id, categoria, nome, custo, preco, quantidade) VALUES (?, ?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [produto.id, produto.categoria, produto.nome, produto.custo, produto.preco, produto.quantidade])

    def get_custo_total(self):
        custo_total = 0.0

        query = "SELECT custo, quantidade FROM produto;"
        resultados = self.cassandra_session.execute(query)

        for resultado in resultados:
            custo = resultado['custo']
            quantidade = resultado['quantidade']
            custo_total += custo * quantidade
        
        return round(custo_total, 2)

    def get_produtos_categoria(self, categoria):
        produtos = []

        query = "SELECT * FROM produto WHERE categoria = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultados = self.cassandra_session.execute(prepared, [categoria])

        for resultado in resultados:
            produto = Produto(
                id=resultado['id'],
                categoria=resultado['categoria'],
                nome=resultado['nome'],
                custo=resultado['custo'],
                preco=round(resultado['preco'], 2),
                quantidade=resultado['quantidade']
            )
            produtos.append(produto)
        
        return produtos

class VendaDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        query = "CREATE TABLE venda(" \
        "id INT," \
        "dia INT," \
        "mes INT," \
        "ano INT," \
        "hora TEXT," \
        "valor FLOAT," \
        "produto_quantidade LIST<frozen<map<int, int>>>," \
        "usuario_id INT," \
        "PRIMARY KEY((dia, mes, ano), hora, id));"
        self.cassandra_session.execute(query)

    def adicionar(self, id: str, data_hora : datetime, usuario_id: int, carrinho : list):
        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year
        hora = data_hora.strftime("%H:%M")
        valor = sum(float(item['preco']) * int(item['quantidade']) for item in carrinho)
        produto_quantidade = [{int(item['id']): int(item['quantidade'])} for item in carrinho]

        query = "INSERT INTO venda(id, dia, mes, ano, hora, valor, produto_quantidade, usuario_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [id, dia, mes, ano, hora, round(valor, 2), produto_quantidade, usuario_id])

    def get_vendas(self, data_hora : datetime):
        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year

        vendas = []

        query = "SELECT * FROM venda WHERE dia = ? AND mes = ? AND ano = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultados = self.cassandra_session.execute(prepared, [dia, mes, ano])

        for resultado in resultados:
            venda = Venda(
                id=resultado['id'],
                dia=resultado['dia'],
                mes=resultado['mes'],
                ano=resultado['ano'],
                hora=resultado['hora'],
                valor=round(resultado['valor'], 2),
                produtos = resultado['produto_quantidade']
            )
            vendas.append(venda)
        
        return vendas

usuario_dao = UsuarioDAO()
produto_dao = ProdutoDAO()
        
def test_questao_1_a():

    usuarios = [
        {"id":1, "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua A, 45", "nome":"Serafim Amarantes", "email":"samarantes@g.com", "interesses": ["futebol", "pagode", "engraçado", "cerveja", "estética"]},
        {"id":2, "estado": "São Paulo", "cidade": "São Bento do Sapucaí", "endereco": "Rua B, 67", "nome":"Tamara Borges", "email":"tam_borges@g.com", "interesses": ["estética", "jiujitsu", "luta", "academia", "maquiagem"]},
        {"id":3, "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua C, 84", "nome":"Ubiratã Carvalho", "email":"bira@g.com", "interesses": ["tecnologia", "hardware", "games", "culinária", "servers"]},
        {"id":4, "estado": "Minas Gerais", "cidade": "Pouso Alegre", "endereco": "Rua D, 21", "nome":"Valéria Damasco", "email":"valeria_damasco@g.com", "interesses": ["neurociências", "comportamento", "skinner", "laboratório", "pesquisa"]}
    ]

    output = len(usuarios)


    usuario_dao.criar_tabela()

    for usuario in usuarios:
        usuario_obj = Usuario(
            id=usuario['id'],
            estado=usuario['estado'],
            cidade=usuario['cidade'],
            endereco=usuario['endereco'],
            nome=usuario['nome'],
            email=usuario['email'],
            interesses=usuario['interesses'],
        )
        usuario_dao.adicionar(usuario_obj)

    quantidade_usuarios = usuario_dao.get_quantidade_usuarios()

    assert output == quantidade_usuarios

def teste_questao_1_b():
    produtos = [
        {"id":1, "categoria": "escritório", "nome":"Cadeira HM conforto", "custo": 2000.00, "preco": 3500.00, "quantidade": 120},
        {"id":2, "categoria": "culinária", "nome":"Tábua de corte Hawk", "custo": 360.00, "preco": 559.90, "quantidade": 40},
        {"id":3, "categoria": "tecnologia", "nome":"Notebook X", "custo": 3000.00, "preco": 4160.99, "quantidade": 76},
        {"id":4, "categoria": "games", "nome":"Headset W", "custo": 265.45, "preco": 422.80, "quantidade": 88},
        {"id":5, "categoria": "tecnologia", "nome":"Smartphone X", "custo": 2000.00, "preco": 3500.00, "quantidade": 120},
        {"id":6, "categoria": "games", "nome":"Gamepad Y", "custo": 256.00, "preco": 519.99, "quantidade": 40},
        {"id":7, "categoria": "estética", "nome":"Base Ismusquim", "custo": 50.00, "preco": 120.39, "quantidade": 76},
        {"id":8, "categoria": "cerveja", "nome":"Gutten Bier IPA 600ml", "custo": 65.45, "preco": 122.80, "quantidade": 88}
    ]

    output = 765559.20

    produto_dao.criar_tabela()

    for produto in produtos:
        produto_obj = Produto(
            id=produto['id'],
            categoria=produto['categoria'],
            nome=produto['nome'],
            custo=produto['custo'],
            preco=produto['preco'],
            quantidade=produto['quantidade']
        )
        produto_dao.adicionar(produto_obj)

    custo_total = produto_dao.get_custo_total()

    assert output == custo_total

def test_questao_2():

    estado = "Minas Gerais"

    output = [
        {"id":'1', "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua A, 45", "nome":"Serafim Amarantes", "email":"samarantes@g.com", "interesses": ["futebol", "pagode", "engraçado", "cerveja", "estética"]},
        {"id":'3', "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua C, 84", "nome":"Ubiratã Carvalho", "email":"bira@g.com", "interesses": ["tecnologia", "hardware", "games", "culinária", "servers"]},
        {"id":'4', "estado": "Minas Gerais", "cidade": "Pouso Alegre", "endereco": "Rua D, 21", "nome":"Valéria Damasco", "email":"valeria_damasco@g.com", "interesses": ["neurociências", "comportamento", "skinner", "laboratório", "pesquisa"]}
    ]

    usuarios = usuario_dao.get_usuarios_estado(estado)

    for usuario_obj in usuarios:
        usuario_dao.adicionar_cache(usuario_obj)

    usuarios_cache_dict = [usuario_cache.to_dict() for usuario_cache in usuario_dao.get_cache()]

    assert output == sorted(usuarios_cache_dict, key=lambda d: d['id'])

def test_questao_3():

    usuario_id = 3

    output = [
        {"id":2, "nome":"Tábua de corte Hawk", "preco": 559.90},
        {"id":3, "nome":"Notebook X", "preco": 4160.99},
        {"id":4, "nome":"Headset W", "preco": 422.80},
        {"id":5, "nome":"Smartphone X", "preco": 3500.00},
        {"id":6, "nome":"Gamepad Y", "preco": 519.99}
    ]

    interesses = usuario_dao.get_interesses_cache(usuario_id)
    produtos_dict = []
    for interesse in interesses:
        produtos = produto_dao.get_produtos_categoria(interesse)
        for produto in produtos:
            produto_dict = {
                "id": produto.id,
                "nome": produto.nome,
                "preco": produto.preco
            }
            produtos_dict.append(produto_dict)

    assert output == sorted(produtos_dict, key=lambda d: d['id'])

def test_questao_4():

    usuario_id = 3

    carrinho = [
        {"id":'4', "nome":"Headset W", "preco": '422.80', "quantidade": '1'},
        {"id":'6', "categoria": "games", "nome":"Gamepad Y", "preco": '519.99', "quantidade": '2'},
    ]

    usuario_dao.adicionar_carrinho_cache(usuario_id, carrinho)

    carrinho_cache = usuario_dao.get_carrinho_cache(usuario_id)

    assert carrinho == sorted(carrinho_cache, key=lambda d: d["id"])

venda_dao = VendaDAO()

def test_questao_5():

    usuario_id = 3
    data_hora = datetime.now()

    output = [{"usuario_id": 3, 'hora': data_hora.strftime("%H:%M"), 'valor': 1462.78}]

    venda_dao.criar_tabela()

    carrinho_cache = usuario_dao.get_carrinho_cache(usuario_id)

    venda_dao.adicionar(1, data_hora, usuario_id, carrinho_cache)

    vendas = venda_dao.get_vendas(data_hora)

    assert output == sorted(vendas, key=lambda d: d["hora"])