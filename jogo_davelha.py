"""Esse é o exercicio 1, jogo da velha 4x4, o programa contém 3 funções para funcionar, e o menu, a função jogar, a ganhou e a printar jogo"""

def jogar():
    """Essa função faz o jogo acontecer, ela chama as outras funções, primeiramente ela verifica com a função ganhou() se o jogo ainda não acabou
    em seguida determina pela variavel jogada%2 + 1 (que resulta em 1 ou 2) de qual jogador é a vez, então imprime o tabuleiro, computa a jogada e verifica 
    se o jogador ganhou ou se acabaram as jogadas"""
    jogada=0

    while ganhou() == 0:
        print("Jogador ", jogada%2 + 1)
        printar_jogo()

        linha  = int(input("Linha :"))
        while(linha > 4 or linha < 1):
            linha = int(input("Número inválido, entre com um número de 1 a 4\n"))

        coluna = int(input("Coluna:"))
        while (coluna > 4 or coluna < 1):
            coluna = int(input("Número inválido, entre com um número de 1 a 4\n"))

        if tabuleiro[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1
            else:
                tabuleiro[linha-1][coluna-1]=-1
        else:
            print("Esta posição já está ocupada, jogue novamente.")
            jogada -=1

        if ganhou():
            print("Jogador ",jogada%2 + 1," ganhou após ", jogada+1," rodadas")

        jogada +=1
        if jogada == 16:
            printar_jogo()
            print("Deu velha.")
            return
    
def ganhou():
    """O tabuleiro é formado por números 0, se for a vez do jogador 1, a posição jogada recebe 1, se for o jogador 2, a posição recebe -1
    então os jogadores para ganhar precisam atingir 4 ou -4 "pontos", se isso acontecer a função retorna 1, que será verificado na função jogar.
    essa função verifica as linhas, as colunas e as diagonais"""
    #checando linhas
    for i in range(4):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]+tabuleiro[i][3]
        if soma==4 or soma ==-4:
            return 1

     #checando colunas
    for i in range(4):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]+tabuleiro[3][i]
        if soma==4 or soma ==-4:
            return 1

    #checando diagonais
    diagonal1 = 0
    diagonal2 = 0
    for i in range(4):
        diagonal1 += tabuleiro[i][i]
        y = 3
        diagonal2 = tabuleiro[i][y-i]
    
    if diagonal1==4 or diagonal1==-4 or diagonal2==4 or diagonal2==-4:
        return 1

    return 0

def printar_jogo():
    """Essa função imprime o tabuleiro, 0 significa que a posição não foi ocupada então imprime um _, 1 significa que a posição está ocupada com um x, e -1 com bolinha"""
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" X ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end=' ')

        print()
                

tabuleiro = [ [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0] ]

opcao=1
print("Bem vindo ao jogo da velha")
while opcao != 0:
    opcao = int(input("1. Jogar \n0. Sair\n"))
    if opcao == 1:
        jogar()
    else:
            print("Obrigado por jogar.")