Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
import flask
import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/pegar', methods=['GET'])
def get_tasks():
    BD = ""
    with open("BDJson/BDJason.json", "r")as f:
        BD = json.loads(f.read())
    return jsonify(BD)
@app.route('/mudar', methods=['POST', 'PUT'])
def post_tasks():
    BD = ""
    print(request.json)
    DadoNovo = ""
    with open("BDJson/BDJason.json", "r")as f:
        BD = json.loads(f.read())
        # print("Banco de dados: ",BD)
    try:
        DadoNovo=json.loads(request.json)
    except:
        DadoNovo=request.json
    for key in DadoNovo:
        BD[key]=DadoNovo[key]
    BD=json.dumps(BD)
    with open("BDJson/BDJason.json","w")as f:
        f.write(BD)
    return jsonify(BD)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
