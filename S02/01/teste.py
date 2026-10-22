from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client["dbworld"]
collection = db['countries']

#Exercício 1
#Retorne o nome comum e a capital de todos os países da região "Americas" que não são landlocked, 
# ordenados alfabeticamente pelo nome comum.
paises = collection.find({"region":"Americas", "landlocked":False}, {"_id":0, "name.common":1, "capital":1}).sort("common.name", 1)
for pais in paises:
    print(pais)

print('\n Exercício 2:')
#Exercício 2
#Retorne o nome oficial e a área dos países que fazem fronteira com o Brasil (ou seja, que têm "BRA" em borders),
#  ordenados do maior para o menor por área.
paises = collection.find({"borders":"BRA"}, {"name.official":1, "_id":0, "area":1}).sort("area",-1)
for pais in paises:
    print(pais)

print("\n Exercício 3:")
#Exercício 3
#Retorne o nome comum e a subregião dos países que falam pelo menos uma dessas línguas: inglês (eng),
#  francês (fra) ou espanhol (spa). Sem duplicatas.
paises = collection.find({"languages":{"$in":["eng", "fra", "spa"]}}, {"name.common":1, "_id":0})
for pais in paises:
    print(pais)
client.close()