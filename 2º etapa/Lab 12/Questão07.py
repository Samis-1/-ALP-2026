import datetime


name_1 = input("Qual o seu nome? ")
data_str1 = input("Digite sua data de nascimento (00/00/0000): ")

name_2 = input("Qual o seu nome? ")
data_str2 = input("Digite sua data de nascimento (00/00/0000): ")

data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

if data1 < data2:
    print(f"{name_1} is older than {name_2}")
else:
    print(f"{name_2} is older than {name_1}")