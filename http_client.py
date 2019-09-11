from flask import Flask
import valet

app = Flask(__name__)

@app.route('/')
def hello_world():
    humidity, temperature = led.get_hum_temp()
    return "umidade: {}\ntemperatura: {}C".format(humidity,temperature)

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
   app.run(host='0.0.0.0', port=80)