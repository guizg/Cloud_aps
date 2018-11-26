import requests
import sys
import json
from flask import jsonify

URL = 'http://localhost:5000'

def listar():
  r = requests.get(URL + '/Tarefa')
  return r.json()

def adicionar(nome):
  payload = json.dumps({"nome": nome})
  headers = {'content-type': 'application/json'}
  r = requests.post(URL + '/Tarefa', data=payload, headers=headers)
  
def buscar(id):
  r = requests.get(URL + '/Tarefa' + f'/{id}')
  return r.json()

def apagar(id):
  r = requests.delete(URL + '/Tarefa' + f'/{id}')

def atualizar(id, nome):
  payload = json.dumps({"nome": nome})
  headers = {'content-type': 'application/json'}
  r = requests.put(URL + '/Tarefa' + f'/{id}', data=payload, headers=headers)


ACTION = sys.argv[1]

if(ACTION == 'listar'):
  r = listar()
  print(r)

elif (ACTION == 'adicionar'):
  lista_nomes = []
  for i in range(2, len(sys.argv)):
    lista_nomes.append(sys.argv[i])
  nome = " ".join(lista_nomes)
  adicionar(nome)

elif (ACTION == 'buscar'):
  id = sys.argv[2]
  r = buscar(id)
  print(r)

elif (ACTION == 'apagar'):
  id = sys.argv[2]
  apagar(id)

elif (ACTION == 'atualizar'):
  id = sys.argv[2]
  lista_nomes = []
  for i in range(3, len(sys.argv)):
    lista_nomes.append(sys.argv[i])
  nome = " ".join(lista_nomes)
  atualizar(id, nome)

else:
  print("ERROR")
  
# python tarefa.py listar - lista tarefas
# python tarefa.py adicionar <tarefa> - adiciona tarefa
# python tarefa.py buscar <id tarefa> - busca tarefa
# python tarefa.py apagar <id tarefa> - apaga tarefa
# python tarefa.py atualizar <id tarefa> <tarefa> - atualiza tarefa
