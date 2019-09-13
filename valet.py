import RPi.GPIO as a
import time
import sys
import os

a.setmode(a.BOARD)

a.setup (12, a.OUT)
a.setup (13, a.OUT)

def parar():
    print('funcao parar acionada')
    a.output (12, a.LOW)
    a.output (13, a.LOW)
def frente():
    print('funcao frente acionada')
    a.output (12, a.HIGH)
    a.output (13, a.LOW)
def tras():
    print('funcao tras acionada')
    a.output (12, a.LOW)
    a.output (13, a.HIGH)
              

while 1:
    resposta = input('digite a funcao que vc qer executar [frente] [tras] [parar]: ')
    if resposta == 'frente':
        frente()
    elif resposta == 'tras':
        tras()
    elif resposta == 'parar':
        parar()
    else:
        print('resposta invalida... Tente novamente')

