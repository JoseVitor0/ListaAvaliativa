"""Esse é o exercicio 3, jogo termo em python, o programa utiliza a biblioteca secrets que serve para escolher uma palavra aleatória da lista
no começo, são definidos os códigos das cores, e a variavel para resetar a cor, (voltar para o padrão)"""

import secrets
arquivo = "lista_palavras.txt"

def le_arquivo(arq):
 
    with open(arq) as f:
        return [linha.strip() for linha in f]



verde = "\033[42m"
amarelo = "\033[43m"
resetar = "\033[0m"
opcao = 1

#aqui são apresentadas as instruções do jogo.
print("Bem vindo ao TERMO\n")
print("Instruções: ")
print(verde + "A" + resetar + ": Letra correta na posição correta.")
print(amarelo + "A" + resetar + ": Letra correta na posição errada.")
print("A: Letra errada na posição errada.")
print("\n")

#aqui o jogo é iniciado, e continua até o usuário digitar 0
while opcao != 0:
    print("1- Jogar")
    print("0- Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:

        lista = le_arquivo(arquivo)
        letras = 5
        palavras = []
        tentativas = 0
        jogadas = 0
        vidas = 6
        palavra_certa = dict() 
        letras_tentadas = set()

        #aqui são separadas as palavras com a quantidade de letras determinada, que no padrão do jogo é 5
        for x in lista:
            if len(x) == letras:
                palavras.append(x)

        palavra_escolhida = secrets.choice(palavras)

        while vidas > 0:
            #imprime os espaços da palavra
            for x in range(letras):
                print("_ ", end=" ")

            #aqui recebe a palavra do usuário e faz a validação de acordo com o numero de letras
            print("\n")
            palavra = str(input(":"))
            while len(palavra) != letras:
                palavra = str(input("Número de letras inserido diferente do número de letras da palavra correta, digite novamente\n"))

            #aqui são registradas as letras já tentadas, que irão ser mostradas futuramente
            for x in palavra:
                letras_tentadas.add(x)

            tentativas += 1
            #aqui é verificado se o usuario acertou a palavra, se sim, a palavra é printada em verde e o programa mostra o numero de tentativas
            if palavra == palavra_escolhida:
                print(verde + palavra_escolhida + resetar)
                print(f"Você ganhou! Número de tentativas: {tentativas}")
                break
            else:
                #aqui o programa verifica letra por letra se a letra foi acertada ou se a letra existe na palavra, o programa guarda num dicionario
                #que tem como chave o indice da letra e valor a cor da letra, verde para letra correta, amarelo para letra na posição errada e preto
                #se não existir a letra na palavra
                for x in range(letras):
                    if palavra[x] == palavra_escolhida[x]:
                        palavra_certa[x] = "verde"
                    else:
                        verifica_letra = palavra_escolhida.find(palavra[x])
                        if verifica_letra != -1:
                            palavra_certa[x] = "amarelo"
                        else:
                            palavra_certa[x] = "preto"

                print("\n")
                #aqui mostra as letras já tentadas
                if tentativas > 0:
                    print("Letras já jogadas")
                    for x in letras_tentadas:
                        print(x, end=" ")
                    print("\n")
                #aqui a palavra tentada é exibida de acordo com a cor registrada anteriormente, sempre que é printado com cor, é necessário resetar a cor
                #para o padrão
                for letra, cor in palavra_certa.items():
                    if cor == "verde":
                        print(verde + palavra[letra]+ resetar, end="")
                    elif cor == "amarelo":
                        print(amarelo + palavra[letra] + resetar, end="")
                    elif cor == "preto":
                        print(palavra[letra], end="")

                vidas -= 1
                #se as vidas do usuario acabarem e ele não acertar, ele perde e o jogo acaba
                if vidas == 0:
                    print(f"\nVocê perdeu, a palavra era {palavra_escolhida}")

            print("\n")
    else:
        print("Saindo...")
