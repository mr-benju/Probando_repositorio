import json

with open("mi_json.json", "r", encoding = "utf-8") as archivo:
    try:
        leer = json.load(archivo)
    except:
        leer = []
with open("mi_json.json", "w") as archivo:
    json.dump(leer,archivo,indent = 4)

