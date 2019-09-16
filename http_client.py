from flask import Flask
import valet
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'projeto vivo'    

@app.route('/abrir')
def frente():
    valet.frente()
    return 'cancela abrindo'
@app.route('/fechar')
def tras():
    valet.tras()
    return 'cancela fechando'
@app.route('/parar')
def parar():
    valet.parar()
    return 'parando motores'

if __name__ == '__main__':
    t1 = threading.Thread(target=valet.botao, args=[])
    t1.start()
    app.run(host='0.0.0.0', port=80)
    