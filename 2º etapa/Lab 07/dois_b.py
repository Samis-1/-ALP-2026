#O erro nesse código é que qualquer númerozinho é > 10, e não vai dar pro usuário digitar 10x
vezes = 0
soma = 0
while vezes != 10:
    num = int(input("Digite um número para somar: "))
    soma += num
    vezes += 1
print(f"A soma total é {soma}")
