from socket import *
CTR="DISP"
servidor ="localhost"
porta= 43210
Conexao= socket(AF_INET,SOCK_STREAM)
Conexao.bind((servidor,porta))

Conexao.listen(3)
#--------------------------------------------------------------------
#REFERENTE A PINAGEM
import RPi.GPIO as pin
import time
mA = 12
mB = 13
sensorFimdeCurso1 = 18
sensorFimdeCurso2 = 32
pin.setmode(pin.BOARD)
pin.setup (mA, pin.OUT)
pin.setup (mB, pin.OUT)
pin.setup (sensorFimdeCurso1, pin.IN)
pin.setup (sensorFimdeCurso2, pin.IN)

m1 = pin.PWM (mA, 1000)
m2 = pin.PWM (mB, 1000)
m1.start(0)
m2.start(0)
#-----------------------------------------------------------
#              COMANDOS DA CATRACA:




while 1:
    print("esperandoConexão...")
    com, cliente = Conexao.accept()
    comandoRecebido = Conexao.recv(14)
    msgRecebida = comandoRecebido.decode('utf-8')

    if msgRecebida == "LEVANTARCATRACA":
        while pin.input(sensorFimdeCurso1) == 0:  # Sensor ultrasonico
            CRT="DISP"
            Conexao.send(bytes(CTR,'utf-8')
            # CONSEGUIR DADOS FINAIS E CALCULAR
            # ENVIAR DADOS
            pin.output(mA, pin.HIGH)
            pin.output(mB, pin.LOW)
            m1.ChangeDutyCycle(100)
            m2.ChangeDutyCycle(0)
            Conexao.close()
    elif msgRecebida == "ABAIXACATRACA":
        while pin.input(sensorFimdeCurso2) == 0:
            CRT="INDS"
            # ARMAZENAR ESTADO DA CATRACA
            # CONSEGUIR DADOS INICIAIS
            pin.output(mA, pin.LOW)
            pin.output(mB, pin.HIGH)
            m1.ChangeDutyCycle(0)
            m2.ChangeDutyCycle(5)
            Conexao.close()
    elif msgRecebida == "EstadoCatraca":
        Conexao.send(bytes(CTR,'utf-8'))
        Conexao.close()
    else:
        print("Erro!")
