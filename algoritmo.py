from classes import *
import os
import time

def AtaquesBolsonaro():
    print("Esses são os ataques de Bolsonaro!")
    print("Qual ataque você deseja usar?")
    print("[1] Soco (O oponente sofre 2 pontos de vida)\n[2] Esquiva (Esquivar do ataque do oponente)\n[3] Facada no Estômago (O oponente sofre 6 pontos de dano)\n[4] Tosse Covid (O ooponente fica doente, sofrendo 2 pontos de dano\n[5] Toma Cloroquina! (Bolsonaro se transforma em jacaré, capaz de dar mordidas que fazem o oponente sofrer 1 ponto de vida)")

    opção = input("- ")
    os.system("cls")

    if opção == "1":
        bolsonaro.Atacar(lula)
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")

    elif opção == "2":
        bolsonaro.Esquivar()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")

    elif opção == "3":
        bolsonaro.FacadaEstomago()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")

    elif opção == "4":
        bolsonaro.TosseCovid()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")

    elif opção == "5":
        bolsonaro.TomaCloroquina()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")       

def AtaquesLula():
    print("Esses são os ataques de Lula!")
    print("Qual ataque você deseja usar?")
    print("[1] Soco (O oponente sofre 2 pontos de vida)\n[2] Esquivar (Esquivar do ataque do oponente)\n[3] Amizade (Lula convoca seus amigos Dilma, Alckimin, Haddad, Alexandre de Moraes e sua esposa Janja para a batalha, os golpes resultam em 5 pontos de vida sofridos pelo oponente)\n[4] Picanha e Cervejinha (Recupera 4 pontos de vida)\n[5] Ajuda dos Gays (Lula é um grande defensor das pessoas LGBTQIAPN+, eles o ajudam na batalha, dando golpes que fazem o oponente sofrer 4 pontos de vida)")

    opção = input("- ")
    os.system("cls")

    if opção == "1":
        lula.Atacar(bolsonaro) 
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")

    elif opção == "2":
        lula.Esquivar()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")

    elif opção == "3":
        lula.Amizade()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")

    elif opção == "4":
        lula.PicanhaCervejinha()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")

    elif opção == "5":
        lula.AjudaGays()
        print(f"HP Bolsonaro: {bolsonaro.getvida()}\nHP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")


print("ESSE É UM JOGO DE LUTA: BOLSONARO VS. LULA!!")
print("Com qual personagem você deseja batalhar?")
print("")
print("======Jogador 1======\n[1] Bolsonaro\n[2] Lula")

escolha = input("- ")
os.system("cls")

if escolha == "1":
    print("Você escolheu o Bolsonaro!")
    print("======Jogador 2======\n        Lula")
    time.sleep(3)
    os.system("cls")
    print("Você está no campo de batalha.")
    time.sleep(2)
    print("À sua frente,")
    time.sleep(2)
    print("Caminhando em sua direção,")
    time.sleep(2)
    print("Lula aparece furioso.")
    time.sleep(2)
    print("Vocês se encaram...")
    time.sleep(2)
    print("Ele quer lutar contra você, está preparado Bolsonaro (Jogador 1)?")
    time.sleep(2)
    print("Você também está preparado, Lula (Jogador 2)?")
    time.sleep(4)
    os.system("cls")
    AtaquesBolsonaro()


if escolha == "2":
    print("Você escolheu o Lula!")
    print("======Jogador 2======\n     Bolsonaro")
    time.sleep(3)
    os.system("cls")
    print("Você está no campo de batalha.")
    time.sleep(2)
    print("À sua frente,")
    time.sleep(2)
    print("Caminhando em sua direção,")
    time.sleep(2)
    print("Bolsonaro aparece furioso.")
    time.sleep(2)
    print("Ele quer lutar contra você, está preparado Lula (Jogador 1)?")
    time.sleep(2)
    print("Você também está preparado, Bolsonaro (Jogador 2)?")
    time.sleep(4)
    os.system("cls")
    AtaquesLula()

while lula.getvida() > 0 or bolsonaro.getvida() > 0:
    if escolha == "1":
        AtaquesLula()
        AtaquesBolsonaro()

        if lula.getvida() <= 0:
            print(f"Bolsonaro venceu, BRASIL ACIMA DE TUDO, DEUS ACIMA DE TODOS!")
            time.sleep(2)
            ("Tente novamente em uma próxima... :(")
            time.sleep(3)
            os.system("cls")
            print(F"Bolsonaro está evoluindo para sua última forma, cuidado...!")
            time.sleep(2)
            ("SUPER BOLSONARO MAÇOM!! >:D")
            os.system("pause")
            break

        
        elif bolsonaro.getvida() <= 0:
            print(f"Lula venceu, FAZ O L!")
            time.sleep(2)
            ("Tente novamente em uma próxima... :(")
            time.sleep(3)
            os.system("cls")
            print("Lula está evoluindo para a sua última forma, cuidado...!")
            time.sleep(2) 
            print("LULA BOTEQUEIRO TOMANDO UMA CERVEJINHA! >:D")
            os.system("pause")
            break


    elif escolha == "2":
        AtaquesBolsonaro()
        AtaquesLula()

        if lula.getvida() <= 0:
            print(f"Bolsonaro venceu, BRASIL ACIMA DE TUDO, DEUS ACIMA DE TODOS!")
            time.sleep(2)
            ("Tente novamente em uma próxima... :(")
            time.sleep(3)
            os.system("cls")
            print(F"Bolsonaro está evoluindo para sua última forma, cuidado...!")
            time.sleep(2)
            ("SUPER BOLSONARO MAÇOM!! >:D")
            os.system("pause")
            break
            
        elif bolsonaro.getvida() <= 0:
            print(f"Lula venceu, FAZ O L!")
            time.sleep(2)
            ("Tente novamente em uma próxima... :(")
            time.sleep(3)
            os.system("cls")
            print("Lula está evoluindo para a sua última forma, cuidado...!")
            time.sleep(2) 
            print("LULA BOTEQUEIRO TOMANDO UMA CERVEJINHA! >:D")
            os.system("pause")
            break
