import RPi.GPIO as a
import time
import sys
import os
import threading

##########################################################
#NAO ESQUECER DE COLOCAR O BTM2 NA FUNCAO 'BOTAO()'      #
#QUANDO O SEGUNDO SENSOR DE FIM DE CURSO FOR IMPLEMENTADO#
##########################################################

mA = 12
mB = 13
sfc1 = 18
sfc2 = 32

a.setmode(a.BOARD)

a.setup (mA, a.OUT)
a.setup (mB, a.OUT)
a.setup (sfc1, a.IN)
a.setup (sfc2, a.IN)


def parar():
    print('funcao parar acionada')
    a.output (mA, a.LOW)
    a.output (mB, a.LOW)
def frente():
    print('funcao frente acionada')
    a.output (mA, a.HIGH)
    a.output (mB, a.LOW)
def tras():
    print('funcao tras acionada')
    a.output (mA, a.LOW)
    a.output (mB, a.HIGH)
def botao():
    while True:
        time.sleep(0.1)
        btm1 = a.input(sfc1)
        btm2 = a.input(sfc2)
        if btm1 == 0:
            parar()

os.system('clear')
if __name__ == '__main__' :
    parar()
    t1 = threading.Thread(target=botao, args=[])
    t1.start()
    while 1:
        resposta = input('digite a funcao que vc qer executar [frente] [tras] [parar]\nSe quiser sair digite [sair]\nSua Resposta: ')
        btm1 = a.input(sfc1)
        btm2 = a.input(sfc2)
        
        if resposta == 'frente':
            frente()
        elif resposta == 'tras':
            tras()
        elif resposta == 'parar':
            parar()
        elif resposta == 'sair':
            os.system('clear')
            exit()
        else:
            print('resposta invalida... Tente novamente')

