from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/magicball/<pergunta>', methods = ['GET'])
def magic(pergunta):
		
		if request.method == 'GET':
            if len(pergunta)%2 == 0:
                return jsonify({"answer": "sim"})
            else:
                return jsonify({"answer": "não"})


@app.route('/healthcheck', methods = ['GET'])
def healthcheck():
	return Response(status=200)
	
app.run(host='0.0.0.0', port=5000, debug=False)