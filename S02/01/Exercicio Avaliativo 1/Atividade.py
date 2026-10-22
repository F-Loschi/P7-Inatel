#%% 
import numpy as np
import threading
import time
import random
from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017/")
# %%
db = cliente["bancoiot"]
collection = db.sensores
#%%
def temperaturaSensor1(intervalo):
    while True:
        resultado = 0
        temp = random.randrange(30, 41)
        if(temp<=38):
            resultado = collection.update_one(
                {"nomeSensor":"Temp1"},
                {"$set":{"valorSensor":temp}}
        )
        else:
            resultado = collection.update_one(
                {"nomeSensor":"Temp1"},
                {"$set":{"valorSensor":temp,
                         "sensorAlarmado":True}}
            )
            print("Atenção! Temperatura muito alta! Verificar sensor 1!")
            break
        if resultado.acknowledged:
            print("Valor do sensor 1 atualizado com sucesso!")
        else:
            print("Falha ao atualizar o valor do sensor 1")
        time.sleep(intervalo)
def temperaturaSensor2(intervalo):
    while True:
        resultado = 0
        temp = random.randrange(30, 41)
        if(temp<=38):
            resultado = collection.update_one(
                {"nomeSensor":"Temp2"},
                {"$set":{"valorSensor":temp}}
        )
        else:
            resultado = collection.update_one(
                {"nomeSensor":"Temp2"},
                {"$set":{"valorSensor":temp,
                         "sensorAlarmado":True}}
            )
            print("Atenção! Temperatura muito alta! Verificar sensor 2!")
            break
        if resultado.acknowledged:
            print("Valor do sensor 2 atualizado com sucesso!")
        else:
            print("Falha ao atualizar o valor do sensor 2")
        time.sleep(intervalo)
def temperaturaSensor3(intervalo):
    while True:
        resultado = 0
        temp = random.randrange(30, 41)
        if(temp<=38):
            resultado = collection.update_one(
                {"nomeSensor":"Temp3"},
                {"$set":{"valorSensor":temp}}
        )
        else:
            resultado = collection.update_one(
                {"nomeSensor":"Temp3"},
                {"$set":{"valorSensor":temp,
                         "sensorAlarmado":True}}
            )
            print("Atenção! Temperatura muito alta! Verificar sensor 3!")
            break
        if resultado.acknowledged:
            print("Valor do sensor 3 atualizado com sucesso!")
        else:
            print("Falha ao atualizar o valor do sensor 3")
        time.sleep(intervalo)
# %%
x = threading.Thread(target = temperaturaSensor1, args=(10,))
x.start()
x = threading.Thread(target = temperaturaSensor2, args=(10,))
x.start()
x = threading.Thread(target = temperaturaSensor3, args=(10,))
x.start()
# %%
