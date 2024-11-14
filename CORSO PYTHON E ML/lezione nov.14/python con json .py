
# filejson= '{"chiave" : "valore", "chiave2": "valore2"}' #diz di stringhe
# #convertito in dizionario
# filejsonconv= json.loads(filejson)
# #riconvertito 
# filejson= json.dumps(filejsonconv)
import json
import requests
risposta=requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
risposta_text=risposta.text

# print(risposta.json()['latitude'])
risposta_json = json.loads(risposta_text)
print(risposta_json['latitude'])