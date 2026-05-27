cont = 5
while cont > 0:
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0:
        continue
    #O comando continue pula a proxima linha quando o número é par e quando ímpar nada acontece
    print(f'{num} é um número ímpar')
