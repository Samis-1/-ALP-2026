import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite > 10 or palpite <= 0:
        continue
    if palpite != secreto:
        chances -= 1
        print("Errou")
    if palpite == secreto:
        print("Acertou")
        break
print("Fim")
