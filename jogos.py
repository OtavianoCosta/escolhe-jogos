import forca
import oiajsd

def escolhe_jogo():
    print("Escolha o seu jogo")

    print("(1) Jogo da Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo quer?"))
    if(jogo == 1):
        print("Jogar jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogar Adivinhacao")
        oiajsd.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()





