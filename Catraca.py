from socket import *
CTR="DISP"
servidor ="0.0.0.0"
porta= 80
Conexao= socket(AF_INET,SOCK_STREAM)
Conexao.bind((servidor,porta))

Conexao.listen(3)
#--------------------------------------------------------------------
#REFERENTE A PINAGEM
import RPi.GPIO as a
import time
mA = 12
mB = 13
sensorFimdeCurso1 = 18
sensorFimdeCurso2 = 32
a.setmode(a.BOARD)
a.setup (mA, a.OUT)
a.setup (mB, a.OUT)
a.setup (sensorFimdeCurso1, a.IN)
a.setup (sensorFimdeCurso2, a.IN)

m1 = a.PWM (mA, 1000)
m2 = a.PWM (mB, 1000)
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
        while a.input(sensorFimdeCurso1) == 0:  # Sensor ultrasonico
            CRT="DISP"
            Conexao.send(bytes(CTR,'utf-8')
            # CONSEGUIR DADOS FINAIS E CALCULAR
            # ENVIAR DADOS
            a.output(mA, a.HIGH)
            a.output(mB, a.LOW)
            m1.ChangeDutyCycle(100)
            m2.ChangeDutyCycle(0)
            Conexao.close()
    elif msgRecebida == "ABAIXARCATRACA":
        while a.input(sensorFimdeCurso2) == 0:
            CRT="INDS"
            # ARMAZENAR ESTADO DA CATRACA
            # CONSEGUIR DADOS INICIAIS
            a.output(mA, a.LOW)
            a.output(mB, a.HIGH)
            m1.ChangeDutyCycle(0)
            m2.ChangeDutyCycle(5)
            Conexao.close()
    elif msgRecebida == "EstadoCatraca":
        Conexao.send(bytes(CTR,'utf-8'))
        Conexao.close()
    else:
        print("Erro!")
