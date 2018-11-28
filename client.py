import requests
import sys
import json
from flask import jsonify


IP = "35.173.221.97"
URL = 'http://'+IP+':5000'


palavras_pergunta = []
for i in range(1, len(sys.argv)):
    palavras_pergunta.append(sys.argv[i])
pergunta = " ".join(palavras_pergunta)

payload = json.dumps({"pergunta": pergunta})
headers = {'content-type': 'application/json'}
r = requests.get(URL + '/magicball', data=payload, headers=headers)

print(r.json()['answer'])