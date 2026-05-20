chances = 5
palavra_secreta = 'batata'
while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1 #Quando vc erra, vc perde uma chance e repete a pergunta
    if palavra == 'batata': #quando acerta o jogo acaba independente de quantas chances ainda tinha
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
    