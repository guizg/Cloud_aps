from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/magicball', methods = ['GET'])
def magic():
    
    if request.method == 'GET':
        pergunta = json.loads(request.data)['pergunta']
        print(pergunta)
        if len(pergunta)%2 == 0:
            return jsonify({"answer": "YES"})
        else:
            return jsonify({"answer": "NO"})


@app.route('/healthcheck', methods = ['GET'])
def healthcheck():
	return Response(status=200)
	
app.run(host='0.0.0.0', port=5000, debug=False)