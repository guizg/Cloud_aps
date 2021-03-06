from flask import Flask, request, jsonify, Response
import json

dic = {}
counter = 0

class Tarefa:
	def __init__(self, id, nome):
		self.id = id
		self.nome = nome


app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/Tarefa', methods = ['POST', 'GET'])
def tarefa():
	global counter
	global dic
	if request.method == 'POST':
		# print((request.data))
		nome = json.loads(request.data)['nome']
		print(nome)
		t = Tarefa(counter, nome)

		dic[counter] = nome
		counter +=1
		return Response(status=200)
			
	elif request.method == 'GET':
		return jsonify(dic)

@app.route('/Tarefa/<id>', methods = ['PUT', 'GET', 'DELETE'])
def tarefa_id(id):
	global counter
	global dic
	if request.method == 'DELETE':
		for key in dic:
			if(int(key) == int(id)):
					
				del dic[int(key)]
				print(dic)		
				break
		return Response(status=200)

	elif request.method == 'GET':
		return jsonify(dic[int(id)])

	elif request.method == 'PUT':
		print(json.loads(request.data))
		nome = json.loads(request.data)['nome']
		dic[int(id)] = nome
		print(dic)
		return Response(status=200)


@app.route('/healthcheck', methods = ['GET'])
def healthcheck():
	return Response(status=200)
	
app.run(host='0.0.0.0', port=5000, debug=False)