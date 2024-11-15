#import json

# filejson= '{"chiave" : "valore", "chiave2": "valore2"}' #diz di stringhe
# #convertito in dizionario
# filejsonconv= json.loads(filejson)
# #riconvertito 
# filejson= json.dumps(filejsonconv)

#######################################################################################################################################################
# CON WEB

import json
import requests
#
risposta=requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m") #LINK
risposta_text=risposta.text  #TESTO
# print(risposta.json()['latitude'])
risposta_json = json.loads(risposta_text) #DIZIONARIO 
print(risposta_json['latitude']) #STAMPO LA CHIAVE DI INTERESSE