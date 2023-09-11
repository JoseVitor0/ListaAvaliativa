"""Esse é o exercicio 2, jogo da velha n x n, ele segue os mesmos principios do jogo com dimensões fixas, a primeira coisa é perguntar 
ao usuario o tamanho do jogo, esse tamanho será usado em todas as funções, em seguida o programa cria o tabuleiro com o tamanho selecionado
e inicia as posições do tabuleiro com 0 para seguir a lógica do exercicio anterior"""

def jogar(tamanho):
    """A função jogar faz o jogo acontecer, segue a mesma lógica do exercicio anterior, mas com a variavel tamanho, que é recebida no inicio do programa"""
    jogada=0
    while ganhou(tamanho) == 0:
        print("Jogador ", jogada%2 + 1)
        printar_jogo(tamanho)

        linha  = int(input("Linha :"))
        while(linha > tamanho or linha < 1):
            linha = int(input("Número inválido, entre com um número de 1 a 4\n"))

        coluna = int(input("Coluna:"))
        while (coluna > tamanho or coluna < 1):
            coluna = int(input("Número inválido, entre com um número de 1 a 4\n"))

        if tabuleiro[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1
            else:
                tabuleiro[linha-1][coluna-1]=-1
        else:
            print("Esta posição já está ocupada, jogue novamente.")
            jogada -=1

        if ganhou(tamanho):
            print("Jogador ",jogada%2 + 1," ganhou após ", jogada+1," rodadas")

        jogada +=1
        if jogada == tamanho ** 2:
            printar_jogo(tamanho)
            print("Deu velha.")
            return
    
def ganhou(tamanho):
    """Essa função verifica se o jogador ganhou, verificando as linhas, colunas e diagonais, de acordo com o tamanho, considerando o maximo
    de pontos que pode ser atingido"""
    soma = 0
    #checando linhas
    for x in range(tamanho):
        for y in range(tamanho):
            soma += tabuleiro[x][y]
            if soma==tamanho or soma ==-tamanho:
                return 1

     #checando colunas
    for x in range(tamanho):
        for y in range(tamanho):
            soma += tabuleiro[y][x]
            if soma==tamanho+1 or soma ==-tamanho:
                return 1

    #checando diagonais
    diagonal1 = 0
    diagonal2 = 0
    for x in range(tamanho):
        diagonal1 += tabuleiro[x][x]
        y = tamanho - 1
        diagonal2 = tabuleiro[x][y-x]
    
    if diagonal1==tamanho or diagonal1==-tamanho or diagonal2==tamanho or diagonal2==-tamanho:
        return 1

    return 0

def printar_jogo(tamanho):
    """Essa função imprime o tabuleiro, de acordo com o tamanho, verificando se a posição está ocupada com 0, 1 ou -1, para imprimir _ X ou O"""
    print("\n")
    for i in range(tamanho):
        for j in range(tamanho):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" X ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end=' ')

        print()
    print("\n")
                

tabuleiro = []

opcao=1
print("Bem vindo ao jogo da velha")
while opcao != 0:
    opcao = int(input("1. Jogar \n0. Sair\n"))
    if opcao == 1:
        #aqui é recebida a variavel tamanho, que ditará as proporções do jogo, e servirá de parametro para todas as outras funções
        tamanho = int(input("Qual a quantidade de linhas e colunas do jogo? "))
        tabuleiro = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        jogar(tamanho)
    else:
        print("Obrigado por jogar.")