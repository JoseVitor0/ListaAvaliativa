"""Esse é o exercício 4, banco de dados com dicionarios, foram usados dicionarios, listas, tuplas, apenas conteúdos vistos nas aulas
o programa começa pedindo os campos obrigatórios, em seguida imprime o menu, e então direciona para a função correspondente, na função cadastrar
o usuário pode cadastrar campos adicionais, quantos quiser, após isso são gerados os dicionariuos, na função imprimir, o programa exibe
os usuários com os parametros solicitados"""

banco_usuarios = dict()
id = 0

def cadastrar_usuario(campos_obrigatorios, id):
    """Essa função cadastra os usuários, ela recebe como parâmetros os campos obrigatórios e o id, que é uma variável implementada sempre que é escolhida a opção 1
    o id é usado para diferenciar os cadastros no banco de usuários. a função retorna o dicionario gerado com o cadastro do usuario"""

    novos_campos = []
    dicionario_usuario = dict()
    respostas = []
    print("Cadastrar usuário")

    for x in campos_obrigatorios:
        respostas = input(f"{x}: ")
        dicionario_usuario[x] = respostas

    while respostas != 'sair':
        respostas = input("Deseja cadastrar novos campos? Digite somente o nome do campo. 'sair' para fechar.\n")
        if respostas != 'sair':
            novos_campos.append(respostas)
            novos_campos = novos_campos.lower()

    for x in novos_campos:
        respostas = input(f"{x}: ")
        dicionario_usuario[x] = respostas
       
       
    banco_usuarios[id] = dicionario_usuario

    return dicionario_usuario


def imprimir_usuarios(*args, **kwargs):
    """Essa função imprime os usuários de acordo com os parametros, o primeiro parametro a ser recebido é a opção da impressão, em seguida os campos e valores e/ou os nomes"""
    opcao = kwargs.get('opcao', None)
    campos_filtrar = kwargs.get('campos', None)
    valores_filtrar = kwargs.get('valores', None)
    nomes_filtrar = kwargs.get('nomes', None)

    if opcao == 1:
        #para a opção 1 o programa somente imprime o dicionario completo
        print(banco_usuarios)

    if(opcao == 2):
        #para a opção 2 o programa usa a função items para dividir o dicionario banco usuarios e verifica se os nomes existem no novo dicionario
        for x in args:
            for id, usuario in banco_usuarios.items():
                    if usuario['nome'] == x:
                        print(usuario)
            
    elif opcao == 3:
        #na opção 3 o programa verifica se os campos e os valores existem no novo dicionario, e coloca no dicinario resultados, e em seguida imprime ele
        resultados = {}
        for id, usuario in banco_usuarios.items():
            correspondente = True
            for campo, valor in zip(campos_filtrar, valores_filtrar):
                if campo in usuario and usuario[campo] != valor:
                    correspondente = False
                    break
            if correspondente:
                resultados[id] = usuario

        if resultados:
            print(resultados)
        else:
            print("Não foram encontrados usuários com os critérios desejados")

    elif opcao == 4:
        #na opção 4 o programa verifica se os nomes buscados existem e em seguida faz a mesma comparação dos campos e valores da opção anterior e também coloca no dicionario resultados
        
        resultados = {}
        for id, usuario in banco_usuarios.items():
            correspondente = True
            for nome in nomes_filtrar:
                if nome not in usuario.get('nome', ''):
                    correspondente = False
                    break
            for campo, valor in zip(campos_filtrar, valores_filtrar):
                if campo in usuario and usuario[campo] != valor:
                    correspondente = False
                    break
            if correspondente:
                resultados[id] = usuario
        if resultados:
            print(resultados)
        else:
            print("Não foram encontrados usuários com os critérios desejados")
                    


opcao = 1
campos = []
resposta = []
#recebe os campos obrigatóris para o cadastro, deixa minusculo para não haver erros e coloca na tupla campos
resposta = input("Digite os campos serão obrigatórios para o cadastro (separados por espaço): ")
resposta = resposta.lower()
campos = resposta.split(' ')
tupla = tuple(campos)

while opcao != 0:
    #menu do programa
    print("1- cadastrar usuário.")
    print("2- imprimir usuários.")
    print("0- sair.")
    opcao = int(input("Escolha uma opção: "))
    #para cada opção é requisitado os devidos parametros e iniciado a função com os mesmos
    if (opcao == 1):
        id += 1
        cadastrar_usuario(tupla, id)

    elif(opcao == 2):
        print("1- Imprimir todos.")
        print("2- Filtrar por nomes.")
        print("3- Filtrar por campos.")
        print("4- Filtrar por nomes e campos")

        sub_opcao = int(input("Escolha uma opção: "))
        if(sub_opcao == 1):
            imprimir_usuarios(opcao=sub_opcao)
        elif(sub_opcao == 2):
            nomes = input("Digite os nomes a serem buscados (separados por espaço): ").split()
            imprimir_usuarios(opcao=sub_opcao, *nomes)
        elif (sub_opcao) == 3:
            campos = input("Digite os campos a serem buscados (separados por espaço): ").split()
            valores = input("Digite os valores correspondentes (separados por espaço): ").split()
            imprimir_usuarios(opcao=sub_opcao, campos=campos, valores=valores)
        elif (sub_opcao) == 4:
            nomes = input("Digite os nomes a serem buscados (separados por espaço): ").split()
            campos = input("Digite os campos a serem buscados (separados por espaço): ").split()
            valores = input("Digite os valores correspondentes (separados por espaço): ").split()
            imprimir_usuarios(opcao=sub_opcao, nomes=nomes, campos=campos, valores=valores)

            
