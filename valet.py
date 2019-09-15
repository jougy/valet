import RPi.GPIO as a
import time
import sys
import os

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
    btm2 = a.input(sfc2)
    print('funcao tras acionada')
    a.output (mA, a.LOW)
    a.output (mB, a.HIGH)

if __name__ == '__main__' :
    parar()
    while 1:
        resposta = input('digite a funcao que vc qer executar [frente] [tras] [parar]: ')
        btm1 = a.input(sfc1)
        btm2 = a.input(sfc2)
        
        if resposta == 'frente':
            while btm1 != 0:
                frente()
                btm1 = a.input(sfc1)
            parar()
        elif resposta == 'tras':
            while btm2 !=0:
                tras()
                btm2 = a.input(sfc2)
            parar()
        elif resposta == 'parar':
            parar()
        else:
            print('resposta invalida... Tente novamente')

