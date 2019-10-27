import json
with open("BDJason.json","w") as arquivo:
    Dicionario={"HoraEntradaCatraca1": "inicio: ", "HoraEntradaCatraca2": "inicio: ", "HoraEntradaCatraca3": "inicio: ", "HoraEntradaCatraca4": "inicio: ",
                 "HoraEntradaMediaCatraca1": 0, "HoraEntradaMediaCatraca2": 0, "HoraEntradaMediaCatraca3": 0, "HoraEntradaMediaCatraca4": 0, "HoraSaidaCatraca1": "inicio: ",
                 "HoraSaidaCatraca2": "inicio: ", "HoraSaidaCatraca3": "inicio: ", "HoraSaidaCatraca4": "inicio: ", "HoraSaidaMediaCatraca1": 0, "NPessoasCatraca1": 21,
                 "NPessoasCatraca2": 0, "NPessoasCatraca3": 0, "NPessoasCatraca4": 0, "TempoIndividualCatraca1": "", "TempoIndividualCatraca2": "",
                 "TempoIndividualCatraca3": "", "TempoIndividualCatraca4": "", "TempoMedioCatraca1": 0, "TempoMedioCatraca2": 0, "TempoMedioCatraca3": 0,
                 "TempoMedioCatraca4": 0, "TempoTotalCatraca1": 0, "TempoTotalCatraca2": 0, "TempoTotalCatraca3": 0, "TempoTotalCatraca4": 0,
                 "ComandoAbrireFechar1": "Levanta", "ComandoAbrireFechar2": "Levanta", "ComandoAbrireFechar3": "Levanta", "ComandoAbrireFechar4": "Levanta",
                 "EstadoCatraca1": "Indisponivel", "EstadoCatraca2": "Disponivel", "EstadoCatraca3": "Disponivel", "EstadoCatraca4": "Disponivel"}

    arquivo.write(json.dumps(Dicionario))
