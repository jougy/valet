from socket import *
import time
servidor = "127.0.0.1"
portaSaida = 43210
conexao = socket(AF_INET, SOCK_STREAM)
conexao.bind((servidor, portaSaida))
conexao.listen(20)
#-------------------------------------------------------------------------------------
#                      CRIANDO ARQUIVOS:

with open("NPessoas.txt", "w") as arquivoNPessoas:
    arquivoNPessoas.write(str(0))
with open("TempoTotal.txt", "w") as arquivoTempoTotal:
    arquivoTempoTotal.write(str(0))
with open("TempoMedio.txt", "w") as arquivoTempoMedio:
    arquivoTempoMedio.write(str(0))
with open("TempoIndividual.txt", "a") as arquivoTempoIndividual:
    arquivoTempoIndividual.write(str(0))
with open("HoraEntrada.txt", "a") as arquivoHrEntrada:
    arquivoHrEntrada.write("INICIO: ")
with open("HoraEntradaMedia.txt", "w") as arquivoHrEntradaMedia:
    arquivoHrEntradaMedia.write(str(0))
with open("HoraSaida.txt", "a") as arquivoHrSaida:
    arquivoHrSaida.write("INICIO : ")
with open("HoraSaidaMedia.txt", "w") as arquivoHrSaidaMedia:
    arquivoHrSaidaMedia.write(str(0))
with open("EstadoCatraca1.txt", "w") as arquivoestadocatraca:
    arquivoestadocatraca.write("DIS1")
with open("EstadoCatraca2.txt", "w") as arquivoestadocatraca:
    arquivoestadocatraca.write("DIS2")
with open("EstadoCatraca3.txt", "w") as arquivoestadocatraca:
    arquivoestadocatraca.write("DIS3")
with open("EstadoCatraca4.txt", "w") as arquivoestadocatraca:
    arquivoestadocatraca.write("DIS4")
 #-------------------------------------------------------------------------------------
while 1:
    print("Esperando ordens...")
    com,client= conexao.accept()
    comandoRecebido =com.recv(12)
    comando=comandoRecebido.decode('utf-8')
    comandoRecebido = com.recv(4)
    dado=comandoRecebido.decode('utf-8')
    print("Comando Recebido : ",comando,"Dados Recebidos : ",dado)
 # ****************************************************
 #                  BANCO DE DADOS:


 # NUMERO DE PESSOAS INDIVIDUAL:
    if comando == "NpplCrt1None":
        with open("NPessoas.txt", "r") as arquivoNPessoasLer:
            x = int(arquivoNPessoasLer.read())
            y=x+1
            with open("NPessoas.txt", "w") as arquivoNPessoas:
                arquivoNPessoas.write(str(y))
                dado=comandoRecebido=comando=0






 #******************************************************
     # REFERENTE AO TEMPO DE USO:






         #       TEMPO TOTAL

    elif comando=="TimeTeptCtr1":
            with open("TempoTotal.txt", "r") as arquivoTempoTotaller:
                x=float(arquivoTempoTotaller.read())
                y=float(dado)
                with open("TempoTotal.txt", "w") as arquivoTempoTotal:

                    arquivoTempoTotal.write(str(float(x + y)))
                    comandoRecebido=dado=comando=0




                 # TEMPO MEDIO:
    elif comando=="TimeTepmCtr1":

        with open("TempoTotal.txt", "r") as arquivoTempoTotal:
            x=float(arquivoTempoTotal.read())
            with open("NPessoas.txt", "r") as arquivoNPessoas:
                y=float(arquivoNPessoas.read())
                with open("TempoMedio.txt", "w") as arquivoTempoMedio:
                    arquivoTempoMedio.write(str(x / y))
                    comandoRecebido=dado=comando=0




                     # TEMPO INDIVIDUAL
    elif comando=="TimeTepiCtr1":

        with open("TempoIndividual.txt", "a") as arquivoTempoIndividual:
            x=str(dado)
            arquivoTempoIndividual.write(str(dado + "," ))
            dado=comandoRecebido=comando=0





 #**************************************************************
     # REFERENTE A HORA :



                 #HORA DE ENTRADA NA CATRACA
    elif comando == "HourEntrCtr1":


        with open("HoraEntrada.txt", "a") as arquivoHrEntrada:
            x=str(dado)
            arquivoHrEntrada.write(str(x + ","))
            comandoRecebido=dado=comando=0




                     #HORA DE SAIDA DA CATRACA
    elif comando =="HoursaidCtr1":

        with open("HoraSaida.txt", "a") as arquivoHrSaida:
            x=str(dado)
            arquivoHrSaida.write(str(x+","))
            comandoRecebido=dado=comando=0


    elif comando == "HourMedeCtr1":

        with open("HoraEntrada.txt", "r") as arquivoHrEntrada:
            listaHorarios = [str(arquivoHrEntrada.read())]
            hr00 = listaHorarios.count("0")
            hr01 = listaHorarios.count("1")
            hr02 = listaHorarios.count("2")
            hr03 = listaHorarios.count("3")
            hr04 = listaHorarios.count("4")
            hr05 = listaHorarios.count("5")
            hr06 = listaHorarios.count("6")
            hr07 = listaHorarios.count("7")
            hr08 = listaHorarios.count("8")
            hr09 = listaHorarios.count("9")
            hr10 = listaHorarios.count("10")
            hr11 = listaHorarios.count("11")
            hr12 = listaHorarios.count("12")
            hr13 = listaHorarios.count("13")
            hr14 = listaHorarios.count("14")
            hr15 = listaHorarios.count("15")
            hr16 = listaHorarios.count("16")
            hr17 = listaHorarios.count("17")
            hr18 = listaHorarios.count("18")
            hr19 = listaHorarios.count("19")
            hr20 = listaHorarios.count("20")
            hr21 = listaHorarios.count("21")
            hr22 = listaHorarios.count("22")
            hr23 = listaHorarios.count("23")

            listaCalculada = [hr00, hr01, hr02, hr03, hr04, hr05, hr06, hr07, hr08, hr09, hr10, hr11, hr12,
                              hr13, hr14, hr15, hr16, hr17, hr18, hr19, hr20, hr21, hr22, hr23]
            x = int(listaCalculada.max())
            with open("HoraEntradaMedia.txt", "W") as arquivoHrEntradaMedia:
                arquivoHrEntradaMedia.write(str(x))
                comandoRecebido = dado = comando=0






    elif comando == "HourMedsCtr1":

        with open("HoraSaida.txt", "r") as arquivoHrSaida:
            listaHorarios = [str(arquivoHrEntrada.read())]
            hr00 = listaHorarios.count("0")
            hr01 = listaHorarios.count("1")
            hr02 = listaHorarios.count("2")
            hr03 = listaHorarios.count("3")
            hr04 = listaHorarios.count("4")
            hr05 = listaHorarios.count("5")
            hr06 = listaHorarios.count("6")
            hr07 = listaHorarios.count("7")
            hr08 = listaHorarios.count("8")
            hr09 = listaHorarios.count("9")
            hr10 = listaHorarios.count("10")
            hr11 = listaHorarios.count("11")
            hr12 = listaHorarios.count("12")
            hr13 = listaHorarios.count("13")
            hr14 = listaHorarios.count("14")
            hr15 = listaHorarios.count("15")
            hr16 = listaHorarios.count("16")
            hr17 = listaHorarios.count("17")
            hr18 = listaHorarios.count("18")
            hr19 = listaHorarios.count("19")
            hr20 = listaHorarios.count("20")
            hr21 = listaHorarios.count("21")
            hr22 = listaHorarios.count("22")
            hr23 = listaHorarios.count("23")
            listaCalculada = [hr00, hr01, hr02, hr03, hr04, hr05, hr06, hr07, hr08, hr09, hr10, hr11, hr12,
                              hr13, hr14, hr15, hr16, hr17, hr18, hr19, hr20, hr21, hr22, hr23]
            x = int(listaCalculada.max())
            with open("HoraSaidaMedia.txt", "W") as arquivoHrSaidaMedia:

                arquivoHrSaidaMedia.write(str(x))
                comandoRecebido=dado=comando=0

     # *****************************************************
#                   ESTADO DA CATRACA:





    elif comando == "EstdCtr1None":
        x=str(dado)
        with open("EstadoCatraca1.txt", "w") as arquivoestadocatraca:

            arquivoestadocatraca.write(str(x))
            comandoRecebido=dado=comando=0


    elif comando == "EstdCtr2None":
        x = str(dado)
        with open("EstadoCatraca2.txt", "w") as arquivoestadocatraca:
            arquivoestadocatraca.write(str(x))
            comandoRecebido = dado =comando= 0

    elif comando == "EstdCtr3None":
        x = str(dado)
        with open("EstadoCatraca3.txt", "w") as arquivoestadocatraca:
            arquivoestadocatraca.write(str(x))
            comandoRecebido = dado = comando=0

    elif comando == "EstdCtr4None":
        x = str(dado)
        with open("EstadoCatraca4.txt", "w") as arquivoestadocatraca:
            arquivoestadocatraca.write(str(x))
            comandoRecebido = dado = comando=0


                         #   PERGUNTAS:


    elif comando=="EstdCt1?None":

            with open("EstadoCatraca1.txt", "r") as arquivoestadocatraca:
                x=bytes(arquivoestadocatraca.read(),'utf-8')
                comandoRecebido=dado=comando=0
                com.send(x)



    elif comando=="EstCt2?None":
        with open("EstadoCatraca2.txt", "r") as arquivoestadocatraca:
            x=bytes(arquivoestadocatraca.read(),'utf-8')
            com.send(x)
            comandoRecebido=dado=comando=0



    elif comando=="EstCt3?None":
        with open("EstadoCatraca3.txt", "r") as arquivoestadocatraca:
            x=bytes(arquivoestadocatraca.read(),'utf-8')
            com.send(x)
            comandoRecebido=dado=comando=0

    elif comando=="EstCt4?None":

        with open("EstadoCatraca4.txt", "r") as arquivoestadocatraca:
            x=bytes(arquivoestadocatraca.read(),'utf-8')
            com.send(x)
            comandoRecebido=dado=comando=0


    else:


        print("Erro!")
