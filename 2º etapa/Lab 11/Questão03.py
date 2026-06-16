import random
import time
while True:
    print("Deseja fazer uma pergunta de sim ou não?")
    usu = input()
    
    if usu ==  "n" or usu ==  "não" or usu ==  "Não":
        break
    usu = input("Digite a sua pergunta: ")
    prob = random.randint(1, 10)
    time.sleep(2)
    print("Consultando as estrelas...")
    time.sleep(2)
    print("Ligando as constelações...")
    time.sleep(2)
    print("Obtemos a sua resposta!")
    if prob <=5:
        print("Sim")
    else:
        print("Não")
