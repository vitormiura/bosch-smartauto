import random
def oitavas(times_matamata,ganhador_matamata1,ganhador_matamata2,ganhador_matamata3,
            ganhador_matamata4,ganhador_matamata5,ganhador_matamata6,ganhador_matamata7,
            ganhador_matamata8):

    print(" ")
    print(10 * "\033[1;32m-" + "OITAVAS DE FINAL" + 10 * "-")
    print(" \033[1;0m")

    for i in range(0, 8):
        time_escolhido1 = random.choice(times_matamata)
        times_matamata.remove(time_escolhido1)
        time_escolhido2 = random.choice(times_matamata)
        times_matamata.remove(time_escolhido2)

        matamata_chave = time_escolhido1 + " \033[1;91mX \033[1;0m " + time_escolhido2
        print(matamata_chave)

        if ganhador_matamata1 == "":
            ganhador_matamata1 = time_escolhido1

        elif ganhador_matamata2 == "":
            ganhador_matamata2 = time_escolhido2

        elif ganhador_matamata3 == "":
            ganhador_matamata3 = time_escolhido2

        elif ganhador_matamata4 == "":
            ganhador_matamata4 = time_escolhido2

        elif ganhador_matamata5 == "":
            ganhador_matamata5 = time_escolhido1

        elif ganhador_matamata6 == "":
            ganhador_matamata6 = time_escolhido1

        elif ganhador_matamata7 == "":
            ganhador_matamata7 = time_escolhido2

        elif ganhador_matamata8 == "":
            ganhador_matamata8 = time_escolhido1

    times_oitavas_func = [ganhador_matamata1, ganhador_matamata2, ganhador_matamata3, ganhador_matamata4, ganhador_matamata5,
                     ganhador_matamata6, ganhador_matamata7, ganhador_matamata8]

    return times_oitavas_func

def quartas(times_oitavas):
    for i in range(0, 4):
        time_escolhido3 = random.choice(times_oitavas)
        times_oitavas.remove(time_escolhido3)
        time_escolhido4 = random.choice(times_oitavas)
        times_oitavas.remove(time_escolhido4)

        oitavas_chave = time_escolhido3 + " \033[1;91mX \033[1;0m " + time_escolhido4
        print(oitavas_chave)

        if ganhador_oitavas1 == "":
            ganhador_oitavas1 = time_escolhido3

        elif ganhador_oitavas2 == "":
            ganhador_oitavas2 = time_escolhido4

        elif ganhador_oitavas3 == "":
            ganhador_oitavas3 = time_escolhido3

        elif ganhador_oitavas4 == "":
            ganhador_oitavas4 = time_escolhido4

    times_quartas = [ganhador_oitavas1, ganhador_oitavas2, ganhador_oitavas3, ganhador_oitavas4]