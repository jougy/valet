from flask import Flask
import valet

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('projeto vivo')

@app.route('/abrir')
def frente():
    print('cancela abrindo')
    valet.frente()

@app.route('/fechar')
def tras():
    print('cancela fechando')
    valet.tras()
    
@app.route('/parar')
def parar():
    print('parando motores')
    valet.parar()
    

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
