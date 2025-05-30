import os
from time import sleep
from functions.utils import *
from functions import *
      
caminho = os.path.abspath(__file__)
arquivo = str(os.path.dirname(caminho) + r'\Banco_de_dados\Cadastro_de_livros.txt')
print(arquivo)
if not arqExiste(arquivo):
    criarArq(arquivo)

while True:
    menu(['CADASTRAR LIVRO', 'LISTA DE LIVROS/FATURAMENTO', 'VENDER LIVRO', 'FINALIZAR PROGRAMA'])
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        cabecalho('CADASTRAR LIVRO')
        cadastrar(arquivo, nome=input('Nome do livro: '), autor=input('Autor: '), genero=input('Gênero: '),
                quant=int(input('Quantidade: ')), preco=float(input('Preço: ')))
        
    if opcao == 2:
        lerArq(arquivo)

    if opcao == 3:
        lerArq(arquivo)
        venda(arquivo, num_livro=int(input('Qual livro deseja realizar venda?: ')))

    if opcao == 4:
        print('PROGRAMA FINALIZADO')
        break