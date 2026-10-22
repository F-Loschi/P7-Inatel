#%%
from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017/")
#%%
db = cliente["dbworld"]
db
# %%
collection = db.countries
paises = collection.find()
# %%
for pais in paises:
    print(pais)
# %%
#Apenas o nome oficial dos países que são da região "Americas" e possuem área menor que 100
exercicio1 = collection.find({"region": "Americas", "area": {"$lt": 100}},
                             {"name.official":1})
for pais in exercicio1:
    print(pais)

# %%
#O nome comum, a latitude e longitude apenas dos países que falam português(por)
exercicio2 = collection.find({"languages.por":{"$exists":True}},
                             {"name.common":1, 'latlng':1})
for pais in exercicio2:
    print(pais)
#%%
#Mostre apenas o nome comum dos países quem começam com "B"
#e ordene os resultados por ordem crescente de area
exercicio3 = collection.find({"name.common":{"$regex":"^B"}},
                             {"name.common":1, "area":1}).sort("area", 1)
for pais in exercicio3:
    print(pais)
# %%
#Exercício 4 — Países da região "Europe" com área maior que 100.000 km², 
# mostrando nome comum, capital e área, ordenados por área decrescente:
exercicio1 = collection.find({"region": "Europe", "area": {"$gt": 1000000}},
                             {"name.common":1, "capital":1, "area":1}).sort("area",-1)
for pais in exercicio1:
    print(pais)
# %%
new_doc = {
    "name": {"common":"Felidro"},
    "capital":"Maria Laura"
}
result = collection.insert_one(new_doc)

if result.acknowledged:
    print("Funcionou papai")
else:
    print("Deu não")
# %%
ex = collection.find({"name.common": "Felidro"})
for pais in ex:
    print(pais)

# %%
result = collection.update_one(
    {"name.common":"Felidro"},
    {"$set":{"name.common":"Pelipe"}}
)

if result.acknowledged:
    print("Funcionou papai")
else:
    print("Deu não")
# %%
ex = collection.find({"name.common": "Pelipe"})
for pais in ex:
    print(pais)
# %%
result = collection.delete_one({"name.common":"Pelipe"})
if result.acknowledged:
    print("Funcionou papai")
else:
    print("Deu não")
# %%
ex = collection.find({"name.common": "Pelipe"})
for pais in ex:
    print(pais)

# %%
result = collection.update_one(
    {"name.common": "Pelipe"},
    {"$set":{"languages":{"agiu":"Giuli"}}}
)
if result.acknowledged:
    print("Funcionou papai")
else:
    print("Deu não")
# %%
