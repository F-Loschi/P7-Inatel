from datetime import datetime

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

import redis
import json

from s202_np2_revisao_models import Aluno, Curso, Matricula

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
                                
class AlunoDAO:   

    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()
        self.redis_connection = RedisDBConnector.get_connection()
    
    def criar_tabela(self):
        query = " CREATE TABLE alunos(" \
        "id INT," \
        "pais TEXT," \
        "cidade TEXT," \
        "endereco TEXT," \
        "nome TEXT," \
        "email TEXT," \
        "areas_estudo LIST<TEXT>," \
        "PRIMARY KEY((pais, cidade), id));"
        self.cassandra_session.execute(query)

    def adicionar(self, aluno : Aluno):
        query = "INSERT INTO alunos(id, pais, cidade, endereco, nome, email, areas_estudo) VALUES (?, ?, ?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [aluno.id, aluno.pais, aluno.cidade, aluno.endereco, aluno.nome, aluno.email, aluno.areas_estudo])
    
    def get_quantidade_alunos(self):
        query = "SELECT COUNT(*) FROM alunos;"
        resultado = self.cassandra_session.execute(query)
        return resultado[0]["count"]

    def get_alunos_pais(self, pais : str):
        alunos = []
        
        query = "SELECT * FROM alunos WHERE pais = ? ALLOW FILTERING;"# ALLOW FILTERING porque pais é apenas uma parte da partition key
        prepared = self.cassandra_session.prepare(query)
        resultado = self.cassandra_session.execute(prepared, [pais])
        
        for aluno in resultado:
            aluno_obj = Aluno(
            id=aluno['id'],
            pais=aluno['pais'],
            cidade=aluno['cidade'],
            endereco=aluno['endereco'],
            nome=aluno['nome'],
            email=aluno['email'],
            areas_estudo=aluno['areas_estudo'],
            )
            alunos.append(aluno_obj)

        return alunos
    
    def adicionar_cache(self, aluno : Aluno):
        self.redis_connection.hset(f'aluno:{aluno.id}', mapping={'pais':aluno.pais, 'cidade':aluno.cidade,
                                                                 'endereco': aluno.endereco, 'nome':aluno.nome, 'email':aluno.email})
        self.redis_connection.rpush(f'aluno:{aluno.id}:areas', *aluno.areas_estudo) # * desempacota a lista como argumentos separados
        
        
    def get_cache(self):
        alunos = []
        
        chaves = [p for p in self.redis_connection.keys("aluno:*") if not p.endswith("areas")]
        
        for chave in chaves:
            dados = self.redis_connection.hgetall(chave)
            areas = self.redis_connection.lrange(f"{chave}:areas", 0, -1)
            aluno = Aluno(
                id = chave.split(":")[1],
                pais = dados['pais'],
                cidade = dados['cidade'],
                endereco = dados['endereco'],
                nome = dados['nome'],
                email = dados['email'],
                areas_estudo = areas
            )
            alunos.append(aluno)

        return alunos

    def get_areas_estudo_cache(self, aluno_id : int):
        areas = self.redis_connection.lrange(f"aluno:{aluno_id}:areas", 0, -1)
        return areas

    def adicionar_lista_desejos_cache(self, aluno_id : int, lista_desejos : list):
        for desejo in lista_desejos:
            self.redis_connection.rpush(f'desejos:{aluno_id}', json.dumps(desejo))

    def get_lista_desejos_cache(self, aluno_id : int):
        resultado = []

        buscas = self.redis_connection.lrange(f'desejos:{aluno_id}', 0, -1)
        for busca in buscas:
            resultado.append(json.loads(busca))

        return resultado


class CursoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        query = "CREATE TABLE curso(" \
        "id INT," \
        "categoria TEXT," \
        "nome TEXT," \
        "custo_producao DECIMAL," \
        "preco DECIMAL," \
        "duracao_horas INT," \
        "PRIMARY KEY((categoria), id));"
        self.cassandra_session.execute(query)

    def adicionar(self, curso : Curso):
        query = "INSERT INTO curso(id, categoria, nome, custo_producao, preco, duracao_horas) VALUES (?, ?, ?, ?, ?, ?)"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [curso.id, curso.categoria, curso.nome, curso.custo_producao, curso.preco, curso.duracao_horas])
    
    def get_custo_total(self):
        query = "SELECT SUM(custo_producao) FROM curso"
        resultado = self.cassandra_session.execute(query)
        return resultado[0]["system.sum(custo_producao)"]
    
    def get_cursos_categoria(self, categoria):
        cursos = []
        
        query = "SELECT id, nome, preco FROM curso WHERE categoria = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultados = self.cassandra_session.execute(prepared, [categoria])
        
        for resultado in resultados:
            curso = Curso(
                id = resultado['id'],
                nome = resultado['nome'],
                preco = resultado['preco'],
                categoria = None,
                custo_producao = None,
                duracao_horas = None
            )
            cursos.append(curso)

        return cursos

class MatriculaDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def soma_cursos(self, lista_desejos:list)->float:
        preco_final = 0
        
        for desejo in lista_desejos:
            preco_final += float(desejo['preco'])

        return preco_final

    def criar_tabela(self):
        query = "CREATE TABLE matricula(id int," \
        "dia int," \
        "mes int," \
        "ano int," \
        "hora text," \
        "valor_total float," \
        "cursos_quantidade list<frozen<map<int, int>>>," \
        "aluno_id int," \
        "PRIMARY KEY((dia, mes, ano), hora, id));"
        self.cassandra_session.execute(query)

    def adicionar(self, id: str, data_hora : datetime, aluno_id: int, lista_desejos : list):
        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year
        data_hora_strip = data_hora.strftime("%H:%M")
        preco = self.soma_cursos(lista_desejos)
        cursos_quantidade = [{int(desejo['id']): 1} for desejo in lista_desejos]

        query = "INSERT INTO matricula(id, dia, mes, ano, hora, valor_total, cursos_quantidade, aluno_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [id, dia, mes, ano, data_hora_strip, preco, cursos_quantidade, aluno_id])


    def get_matriculas(self, data_hora : datetime):
        resultado = []
        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year

        query = "SELECT * FROM matricula WHERE dia = ? AND mes = ? AND ano = ?;"
        prepared = self.cassandra_session.prepare(query)
        matriculas = self.cassandra_session.execute(prepared, [dia, mes, ano])
        
        for m in matriculas:
            resultado.append({
                "aluno_id" : m['aluno_id'],
                "hora" : m['hora'],
                "valor" : round(float(m['valor_total']),2)
            })

        return resultado

aluno_dao = AlunoDAO()
curso_dao = CursoDAO()
        
def test_questao_1_a():

    alunos = [
        {"id":1, "pais": "Brasil", "cidade": "São Paulo", "endereco": "Av. Paulista, 1000", "nome":"Ana Silva", "email":"ana.silva@email.com", "areas_estudo": ["programação", "web", "python", "banco de dados", "machine learning"]},
        {"id":2, "pais": "Brasil", "cidade": "Rio de Janeiro", "endereco": "Rua Copacabana, 200", "nome":"Carlos Santos", "email":"carlos.santos@email.com", "areas_estudo": ["design", "ui/ux", "frontend", "javascript", "react"]},
        {"id":3, "pais": "Argentina", "cidade": "Buenos Aires", "endereco": "Av. Corrientes, 500", "nome":"María García", "email":"maria.garcia@email.com", "areas_estudo": ["data science", "python", "estatística", "visualização", "big data"]},
        {"id":4, "pais": "Brasil", "cidade": "Belo Horizonte", "endereco": "Rua da Bahia, 300", "nome":"João Oliveira", "email":"joao.oliveira@email.com", "areas_estudo": ["mobile", "android", "kotlin", "ios", "swift"]}
    ]

    output = len(alunos)


    aluno_dao.criar_tabela()

    for aluno in alunos:
        aluno_obj = Aluno(
            id=aluno['id'],
            pais=aluno['pais'],
            cidade=aluno['cidade'],
            endereco=aluno['endereco'],
            nome=aluno['nome'],
            email=aluno['email'],
            areas_estudo=aluno['areas_estudo'],
        )
        aluno_dao.adicionar(aluno_obj)

    quantidade_alunos = aluno_dao.get_quantidade_alunos()

    assert output == quantidade_alunos

def teste_questao_1_b():
    cursos = [
        {"id":1, "categoria": "programação", "nome":"Python Avançado", "custo_producao": 5000.00, "preco": 299.90, "duracao_horas": 40},
        {"id":2, "categoria": "design", "nome":"UI/UX Design", "custo_producao": 3500.00, "preco": 199.90, "duracao_horas": 30},
        {"id":3, "categoria": "data science", "nome":"Data Science com Python", "custo_producao": 6000.00, "preco": 349.90, "duracao_horas": 50},
        {"id":4, "categoria": "mobile", "nome":"Desenvolvimento Android", "custo_producao": 4500.00, "preco": 249.90, "duracao_horas": 35},
        {"id":5, "categoria": "programação", "nome":"JavaScript Moderno", "custo_producao": 4000.00, "preco": 229.90, "duracao_horas": 32},
        {"id":6, "categoria": "design", "nome":"Figma para Iniciantes", "custo_producao": 2500.00, "preco": 149.90, "duracao_horas": 20},
        {"id":7, "categoria": "data science", "nome":"Machine Learning", "custo_producao": 7000.00, "preco": 399.90, "duracao_horas": 60},
        {"id":8, "categoria": "mobile", "nome":"Desenvolvimento iOS", "custo_producao": 5000.00, "preco": 299.90, "duracao_horas": 40}
    ]

    output = 37500.00

    curso_dao.criar_tabela()

    for curso in cursos:
        curso_obj = Curso(
            id=curso['id'],
            categoria=curso['categoria'],
            nome=curso['nome'],
            custo_producao=curso['custo_producao'],
            preco=curso['preco'],
            duracao_horas=curso['duracao_horas']
        )
        curso_dao.adicionar(curso_obj)

    custo_total = curso_dao.get_custo_total()
    
    assert output == custo_total

def test_questao_2():

    pais = "Brasil"

    output = [
        {"id":'1', "pais": "Brasil", "cidade": "São Paulo", "endereco": "Av. Paulista, 1000", "nome":"Ana Silva", "email":"ana.silva@email.com", "areas_estudo": ["programação", "web", "python", "banco de dados", "machine learning"]},
        {"id":'2', "pais": "Brasil", "cidade": "Rio de Janeiro", "endereco": "Rua Copacabana, 200", "nome":"Carlos Santos", "email":"carlos.santos@email.com", "areas_estudo": ["design", "ui/ux", "frontend", "javascript", "react"]},
        {"id":'4', "pais": "Brasil", "cidade": "Belo Horizonte", "endereco": "Rua da Bahia, 300", "nome":"João Oliveira", "email":"joao.oliveira@email.com", "areas_estudo": ["mobile", "android", "kotlin", "ios", "swift"]}
    ]

    alunos = aluno_dao.get_alunos_pais(pais)

    for aluno_obj in alunos:
        aluno_dao.adicionar_cache(aluno_obj)

    alunos_cache_dict = [aluno_cache.to_dict() for aluno_cache in aluno_dao.get_cache()]

    assert output == sorted(alunos_cache_dict, key=lambda d: d['id'])

def test_questao_3():

    aluno_id = 2

    output = [
        {"id":2, "nome":"UI/UX Design", "preco": 199.90},
        #{"id":5, "nome":"JavaScript Moderno", "preco": 229.90},
        {"id":6, "nome":"Figma para Iniciantes", "preco": 149.90}
    ]

    areas_estudo = aluno_dao.get_areas_estudo_cache(aluno_id)
    cursos_dict = []
    for area in areas_estudo:
        cursos = curso_dao.get_cursos_categoria(area)
        for curso in cursos:
            curso_dict = {
                "id": curso.id,
                "nome": curso.nome,
                "preco": curso.preco
            }
            cursos_dict.append(curso_dict)
    
    assert output == sorted(cursos_dict, key=lambda d: d['id'])

def test_questao_4():

    aluno_id = 2

    lista_desejos = [
        {"id":'2', "nome":"UI/UX Design", "preco": '199.90', "duracao_horas": '30'},
        {"id":'6', "categoria": "design", "nome":"Figma para Iniciantes", "preco": '149.90', "duracao_horas": '20'},
    ]

    aluno_dao.adicionar_lista_desejos_cache(aluno_id, lista_desejos)

    lista_desejos_cache = aluno_dao.get_lista_desejos_cache(aluno_id)

    assert lista_desejos == sorted(lista_desejos_cache, key=lambda d: d["id"])

matricula_dao = MatriculaDAO()

def test_questao_5():

    aluno_id = 2
    data_hora = datetime.now()

    output = [{"aluno_id": 2, 'hora': data_hora.strftime("%H:%M"), 'valor': 349.80}]

    matricula_dao.criar_tabela()

    lista_desejos_cache = aluno_dao.get_lista_desejos_cache(aluno_id)

    matricula_dao.adicionar(1, data_hora, aluno_id, lista_desejos_cache)

    matriculas = matricula_dao.get_matriculas(data_hora)

    assert output == sorted(matriculas, key=lambda d: d["hora"])