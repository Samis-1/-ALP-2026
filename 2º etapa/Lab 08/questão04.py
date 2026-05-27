soma = 0
number = 1
while number != 0:
    number = int(input("Digite um número: "))
    if number < 0:
        continue
    soma += number
    if number == 0 or soma >= 100:
        break
print(soma)
