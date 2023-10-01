import os

class Personagens:
    def __init__(self, vida):
        self.vida = vida
    
    def getvida(self):
        return self.vida

    def setvida(self, x, y):
        if y  == "somar":
            if self.vida <= 41:
                self.vida = self.vida + x
                print("É ISSO QUE O POVO QUER, COMPANHEIRO!\nLula come sua picanha e bebe uma cervejinha! (+4 pontos de vida)")

            elif self.vida >= 41:
                print("Vida cheia")
                
        elif y == "subtrair":
            self.vida = self.vida - x
    

    def Esquivar(self):
        print("Você esquivou do ataque")
        os.system("pause")
        os.system("cls")

    def Atacar(self, nome):
        print("POW POW POW\nVocê deu um soco! (-2 pontos de vida)")
        nome.setvida(2, "subtrair")
        os.system("pause")
        os.system("cls")

class Lula(Personagens):
    def Amizade(self):
        print("VAMOS JUNTOS COMPANHEIROS!!!\nJuntos, vocês espancaram Bolsonaro! (-5 pontos de vida)")
        bolsonaro.setvida(5, "subtrair")
        os.system("pause")
        os.system("cls")

    def PicanhaCervejinha(self):
        lula.setvida(4, "somar")
        os.system("pause")
        os.system("cls")

    def AjudaGays(self):
        print("VAMOS TODES JUNTES GAYS!!!\nVocês todes ajudaram Lula dando um golpe forte em Bolsonaro! (-4 pontos de vida)")
        bolsonaro.setvida(4, "subtrair")
        os.system("pause")
        os.system("cls")

class Bolsonaro(Personagens):

    def FacadaEstomago(self):
        print("OLHA A FACA!\nLula levou uma facada e está sangrando! (-5 pontos de vida)")
        lula.setvida(5, "subtrair")
        os.system("pause")
        os.system("cls")

    def TosseCovid(self):
        print("COF COF COF!\nLula se infectou! (-3 pontos de vida)")
        lula.setvida(3, "subtrair")
        os.system("pause")
        os.system("cls")

    def TomaCloroquina(self):
        print("VACINA JAMAIS, VIVA A CLOROQUINA!\nBolsonaro se transforma em jacaré e te dá uma mordida! (-1 pontos de vida)")
        lula.setvida(1, "subtrair" )
        os.system("pause")
        os.system("cls")

lula = Lula(45)
bolsonaro = Bolsonaro(45)