#%%
"""
Lembre-se de instalar a lib para acessar o Cassandra:
    pip install cassandra-driver

Além disso, é necessário baixar o secure-connect-*.zip e o *-token.json e colocar
no mesmo diretório
"""

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
import json

cloud_config = {
    'secure_connect_bundle': 'secure-connect-dbiot.zip' # Nome do arquivo do secure-connect-bundle
}

with open("dbiot-token.json") as f: # Nome do arquivo do token
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


# Rotina para verificar se o Cassandra está funcionando
row = session.execute("select release_version from system.local").one()

if row:
    print(row[0])
else:
    print("An error occurred.")
# %%
