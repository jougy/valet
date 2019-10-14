from socket import *
import time
servidor ="127.0.0.1"
portaSaida = 43210
conexao= socket(AF_INET,SOCK_STREAM)


#-------------------------------------------------------------------------------------

while 1:

    time.sleep(3)
    conexao.connect((servidor, portaSaida))
    msg=b'DADO'
    conexao.send(msg)
    ComandoRecebido =conexao.recv(4)
    msgRecebida=ComandoRecebido.decode('utf-8')
    ComandoRecebido = conexao.recv(4)
    msgRecebida2=ComandoRecebido.decode('utf-8')
    ComandoRecebido = conexao.recv(4)
    msgRecebida3=ComandoRecebido.decode('utf-8')
    ComandoRecebido = conexao.recv(1024)
    msgRecebida4 = ComandoRecebido.decode('utf-8')

# ****************************************************
#                  BANCO DE DADOS:


# NUMERO DE PESSOAS INDIVIDUAL:
    if msgRecebida == "Nppl":
        if msgRecebida2 == "CTR1":

            with open("NPessoas.txt", "w") as arquivoNPessoas:
                with open("NPessoas.txt", "r") as arquivoNPessoasLer:
                    arquivoNPessoas.write(str(int(arquivoNPessoasLer.read()) + 1))
                    conexao.close()



#******************************************************
    # REFERENTE AO TEMPO DE USO:

    elif msgRecebida == "Time":




        #       TEMPO TOTAL
        if msgRecebida2=="TepT":
            if msgRecebida3 == "CTR1":
                with open("TempoTotal.txt", "w") as arquivoTempoTotal:
                    with open("TempoTotal.txt", "r") as arquivoTempoTotaller:
                        arquivoTempoTotal.write(str(float(arquivoTempoTotaller.read() + str(msgRecebida4))))
                        conexao.close()



                # TEMPO MEDIO:
        elif msgRecebida2=="TepM":
            if msgRecebida3 == "CTR1":

                with open("TempoMedio.txt", "w") as arquivoTempoMedio:
                    with open("TempoTotal.txt", "r") as arquivoTempoTotal:
                        with open("NPessoas.txt", "r") as arquivoNPessoas:
                            arquivoTempoMedio.write(str(float(arquivoNPessoas.read()) / float(arquivoTempoTotal.read())))
                            conexao.close()



                    # TEMPO INDIVIDUAL
        elif msgRecebida2=="TepI":
            if msgRecebida3=="CTR1":

                with open("TempoIndividual.txt", "a") as arquivoTempoIndividual:
                    arquivoTempoIndividual.write(str(msgRecebida4) + "," )
                    conexao.close()




#**************************************************************
    # REFERENTE A HORA :
    elif msgRecebida == "Hour":



                #HORA DE ENTRADA NA CATRACA
        if msgRecebida2 == "Entr":
            if msgRecebida3=="CTR1":

                with open("HoraEntrada.txt", "a") as arquivoHrEntrada:
                    arquivoHrEntrada.write(str(1) + "," + str(msgRecebida4))
                    conexao.close()



                    #HORA DE SAIDA DA CATRACA
        elif msgRecebida2 =="said":
            if msgRecebida3=="CTR1":

                with open("HoraSaida.txt", "a") as arquivoHrSaida:
                    arquivoHrSaida.write(str() + "," + str(msgRecebida4))
                    conexao.close()

            elif msgRecebida2 == "medE":
                if msgRecebida3 == "CTR1":
                    with open("HoraEntrada.txt", "r") as arquivoHrEntrada:
                        with open("HoraEntradaMedia.txt", "W") as arquivoHrEntradaMedia:
                            listaHorarios = [arquivoHrEntrada.read()]
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
                            arquivoHrEntradaMedia.write(str(listaCalculada.max()))
                            conexao.close()


            elif msgRecebida2 == "medS":
                if msgRecebida3 == "CTR1":
                    with open("HoraSaida.txt", "r") as arquivoHrSaida:
                        with open("HoraSaidaMedia.txt", "W") as arquivoHrSaidaMedia:
                            listaHorarios = [arquivoHrSaida.read()]
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
                            arquivoHrSaidaMedia.write(str(listaCalculada.max()))
                            conexao.close()









    # *****************************************************
#                  ESTADO DA CATRACA:






    elif msgRecebida == "ESTD":
                # ESTADO DA CATRACA 1:

        if msgRecebida2=="CTR1":
            with open("EstadoCatraca.txt", "w") as arquivoestadocatraca:
                arquivoestadocatraca.write(msgRecebida4)
                conexao.close()




    else:
        conexao.close()







