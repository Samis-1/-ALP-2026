#No código anterior o número do contador não aumentava, deixando o while em um loop infinito.
N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    contador += 1
print(f"Quantidade de ímpares entre 1 e {N}: {impares}")

