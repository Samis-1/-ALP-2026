import random
import time
jgdr1 = 0
jgdr2 = 0
while jgdr1 <= 50 or jgdr2 <= 50:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    palp1 = int(input(f"Jogador 1 ({jgdr1} pontos): Qual o seu palpite para a soma dos dados?"))
    palp2 = int(input(f"Jogador 2 ({jgdr2} pontos): Qual o seu palpite para a soma dos dados?"))
    um = abs(soma - palp1)
    dois = abs(soma - palp2)
    