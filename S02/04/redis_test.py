import redis

redis_conn = redis.Redis(
    host="localhost", port=6379,
    decode_responses=True
)

try:
    redis_conn.ping()
    print("Conectado!")
except redis.ConnectionError:
    print("Falha na conexão.")

redis_conn.set("chave2", "valor2")
print("Recuperado:", redis_conn.get("chave2"))

r=redis_conn

r.set("nome", "Felipe")
r.get("nome")           # 'Felipe'

r.set("contador", 10)
r.incr("contador")      # 11
r.incrby("contador", 5) # 16
r.decr("contador")      # 15

r.append("nome", " Silva")  # 'Felipe Silva'
r.strlen("nome")            # 12

r.hset("user:1", mapping={"nome": "Felipe", "idade": 22, "curso": "Engenharia"})

r.hget("user:1", "nome")        # 'Felipe'
r.hgetall("user:1")             # {'nome': 'Felipe', 'idade': '22', ...}
r.hkeys("user:1")               # ['nome', 'idade', 'curso']
r.hvals("user:1")               # ['Felipe', '22', 'Engenharia']
r.hexists("user:1", "idade")    # True
r.hdel("user:1", "curso")       # deleta o campo 'curso'
r.hincrby("user:1", "idade", 1) # 23

