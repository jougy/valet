import requests as r
import json
import pandas as pd
import time
minutoInicial=0
horaInicial=0
minutoFinal=0
horaFinal=0
minutoMedio=0
horaMedia=0
tempoFinal=0
ipGet="http://192.168.43.227:5000/pegar"
ipPost="http://192.168.43.227:5000/mudar"
#--------------------------------------------------------------------
#REFERENTE A PINAGEM
import RPi.GPIO as pin
import datetime
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
#----------------------------------------------------------------------

while 1:
    time.sleep(0.5)

    Resposta= r.get(ipGet)
    Resposta=json.loads(Resposta.text)
    NovosDados={}
    print(Resposta["ComandoAbrireFechar1"])


    if str(Resposta["ComandoAbrireFechar1"])== "Abaixa":

        print("Abaixando Catraca...")

        minutoInicial = pd.datetime.now().minute
        horaInicial = pd.datetime.now().hour
        while pin.input(sensorFimdeCurso2) == 1:
            pin.output(mA, pin.LOW)
            pin.output(mB, pin.HIGH)
            m1.ChangeDutyCycle(0)
            m2.ChangeDutyCycle(5)
        payload = {"ComandoAbrireFechar1": "Em Espera"}
        payload_em_json = json.dumps(payload)
        response = r.post(ipPost, json=payload_em_json)


    elif str(Resposta["ComandoAbrireFechar1"]) == "Levanta":
        print("Levantando Catraca...")
        minutoFinal = pd.datetime.now().minute
        horaFinal = pd.datetime.now().hour
        minutoMedio = minutoFinal - minutoInicial
        minutoMedio = float(minutoMedio / 60)
        horaMedia = horaFinal - horaInicial
        tempoFinal = float(horaMedia + minutoMedio)
        # Numero de Pessoas:
        numeroDePessoas = int(Resposta["NPessoasCatraca1"])
        NovosDados["NPessoasCatraca1"] = numeroDePessoas + 1

        # Tempo Total:
        TempoTotal = float(Resposta["TempoTotalCatraca1"])
        NovosDados["TempoTotalCatraca1"] = TempoTotal + tempoFinal
        # Tempo Individual:
        x=str(Resposta["TempoIndividualCatraca1"])
        NovosDados["TempoIndividualCatraca1"]=(x+str(TempoTotal)+",")
        # Tempo Médio:
        TempoMedio = float(Resposta["TempoMedioCatraca1"])
        NovosDados["TempoMedioCatraca1"] = str(float(NovosDados["TempoTotalCatraca1"]) / float(NovosDados["NPessoasCatraca1"]))
        # Hora de Entrada:

        NovosDados["HoraEntradaCatraca1"]=(Resposta["HoraEntradaCatraca1"]+str(horaInicial) + ",")

        # Hora Final:
        NovosDados["HoraSaidaCatraca1"]=(Resposta["HoraSaidaCatraca1"]+str(horaFinal)+",")

        #Hora Mais Usada Entrada:


        listaEntrada=Resposta["HoraEntradaCatraca1"].split(",")

        ListaDeValores = {}
        for valor in listaEntrada:
            if valor not in ListaDeValores:
                ListaDeValores[valor] = listaEntrada.count(valor)

        menores = []
        maiores = []
        for valor in ListaDeValores:
            soma = ListaDeValores[valor]
            for verificador in ListaDeValores:
                somatoria = ListaDeValores[verificador]
                if soma > somatoria:
                    if verificador not in menores:
                        menores.append(verificador)
                if valor not in menores:
                    if valor not in maiores:
                        maiores.append(valor)
        for menor in menores:
            if menor in maiores:
                maiores.remove(menor)
                HoraMaisUsada = int(maiores[0])
                NovosDados["HoraEntradaMediaCatraca1"]=HoraMaisUsada
        # Hora Mais Usada Saida:


        listaSaida = Resposta["HoraSaidaCatraca1"].split(",")
        ListaDeValores = {}
        for valor in listaSaida:
            if valor not in ListaDeValores:
                ListaDeValores[valor] = listaSaida.count(valor)

        menores = []
        maiores = []
        for valor in ListaDeValores:
            soma = ListaDeValores[valor]
            for verificador in ListaDeValores:
                somatoria = ListaDeValores[verificador]
                if soma > somatoria:
                    if verificador not in menores:
                        menores.append(verificador)
                if valor not in menores:
                    if valor not in maiores:
                        maiores.append(valor)
        for menor in menores:
            if menor in maiores:
                maiores.remove(menor)
                HoraMaisUsada = int(maiores[0])
                NovosDados["HoraSaidaMediaCatraca1"] = HoraMaisUsada


        print(NovosDados)
        payload = NovosDados
        payload_em_json = json.dumps(payload)
        response = r.post(ipPost, json=payload_em_json)
        print(payload_em_json)
        while pin.input(sensorFimdeCurso1) == 1:
            
            # abaixar Catraca:

            pin.output(mA, pin.HIGH)
            pin.output(mB, pin.LOW)
            m1.ChangeDutyCycle(100)
            m2.ChangeDutyCycle(0)
        payload = {"ComandoAbrireFechar1": "Em Espera"}
        payload_em_json = json.dumps(payload)
        response = r.post(ipPost, json=payload_em_json)


    else:
        time.sleep(0.5)

        Resposta = r.get(ipGet)
        Resposta = json.loads(Resposta.text)
        NovosDados = {}
        print(Resposta["ComandoAbrireFechar1"])
