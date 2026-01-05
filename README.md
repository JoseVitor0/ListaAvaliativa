# Algoritmos em Python 🐍

Este repositório contém uma coleção de **algoritmos simples desenvolvidos em Python**, criados como exercícios de lógica de programação.  
O objetivo dos projetos é praticar conceitos fundamentais da linguagem, como funções, estruturas de dados, controle de fluxo e interação com o usuário.

Todos os exercícios foram desenvolvidos apenas com conteúdos vistos em aula, sem uso de frameworks ou bibliotecas avançadas (exceto quando explicitado).

---

## 📂 Exercícios

### 🎮 Exercício 1 – Jogo da Velha 4x4
Implementação de um jogo da velha com tabuleiro **4x4**.

O programa é estruturado em funções para organizar a lógica do jogo:
- `jogar()` → controla o fluxo da partida  
- `ganhou()` → verifica se algum jogador venceu  
- `printar_jogo()` → exibe o tabuleiro no terminal  

Além disso, há um **menu inicial** para iniciar o jogo.

---

### 🎮 Exercício 2 – Jogo da Velha N x N
Versão generalizada do jogo da velha, onde o usuário define o **tamanho do tabuleiro** (N x N).

Funcionamento:
- O programa pergunta ao usuário o tamanho desejado
- Esse valor é reutilizado em todas as funções
- O tabuleiro é criado dinamicamente
- As posições são inicializadas com `0`, mantendo a lógica do exercício anterior

Esse exercício reforça o uso de **funções reutilizáveis** e **estruturas dinâmicas**.

---

### 🔤 Exercício 3 – Jogo Termo (Wordle) em Python
Implementação de um jogo inspirado no **Termo / Wordle**.

Características:
- Utiliza a biblioteca `secrets` para escolher uma palavra aleatória
- As palavras são selecionadas a partir de uma lista
- O programa define **códigos de cores** para exibir o resultado no terminal
- Há uma variável responsável por **resetar a cor** após cada exibição

O foco do exercício é trabalhar lógica, controle de tentativas e manipulação de strings.

---

### 🗂️ Exercício 4 – Banco de Dados com Dicionários
Simulação de um banco de dados simples utilizando apenas:
- Dicionários
- Listas
- Tuplas  

Fluxo do programa:
- Solicita os **campos obrigatórios** do usuário
- Exibe um **menu de opções**
- Direciona para funções específicas conforme a escolha

Funcionalidades:
- Cadastro de usuários com campos adicionais (quantos o usuário desejar)
- Geração dinâmica de dicionários
- Impressão dos dados conforme parâmetros solicitados

Esse exercício reforça a manipulação de **estruturas de dados** e organização do código.

---

## 🚀 Tecnologias Utilizadas
- Python 3
- Biblioteca padrão (`secrets`)

---

## 🎯 Objetivo do Repositório
Este repositório tem como finalidade:
- Praticar lógica de programação
- Consolidar conceitos básicos de Python
- Servir como histórico de aprendizado e evolução

---

## 📌 Observações
Os códigos foram desenvolvidos com foco educacional e podem ser melhorados futuramente com:
- Tratamento de erros
- Interface gráfica
- Organização em classes
- Testes automatizados

---

✍️ Desenvolvido como parte dos estudos em lógica e programação com Python.
