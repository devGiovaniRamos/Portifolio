def arqExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a=open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo ({nome}) criado com sucesso.')


def cadastrar(arquivo, nome='desconhecido', autor='desconhecido', genero='desconhecido', preco=float(0), quant=int(0), faturamento=float(0)):
    try:
        a=open(arquivo, 'at')
    except:
        'ERRO'
    else:
        a.write(f'{nome};{autor};{genero};{quant};{preco};{faturamento}\n')
        print('Livro cadastrado com sucesso!')
        a.close()


def lerArq(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('Houve um erro ao ler a biblioteca de livros')
    else:
        cont = 0
        for linha in a:
            cont += 1
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{cont}º \033[33mLIVRO:\033[m {dado[0]} \033[33mAUTOR:\033[m {dado[1]} \033[33mGÊNERO:\033[m {dado[2]} \033[33mQUANT:\033[m {dado[3]} \033[33mPREÇO:\033[m R${dado[4]} \033[33mFATURAMENTO:\033[m {float(dado[5]):.2f}')
        a.close()


def venda(arq, num_livro):
    linhas_do_arq = []
    try:
        arquivo=open(arq, 'rt')
        linhas_do_arq = arquivo.readlines()
    except FileNotFoundError:
        print('Houve um erro ao ler a biblioteca de livros')
        return
    else:
        livro_encontrado = False
        for i, linha in enumerate(linhas_do_arq):
            dado = linha.strip().split(';')
            if (i+1) == num_livro:
                livro_encontrado = True
                quant_atual = int(dado[3])
                faturamento = float(dado[5])
                if quant_atual > 0:
                    dado[3] = str(quant_atual - 1)
                    dado[5] = str(faturamento + float(dado[4]))
                    linhas_do_arq[i] = ';'.join(dado) + '\n'
                    print('\033[32mVenda realizada com sucesso!\033[m')
                else:
                    print(f'O livro "{dado[0]}" está esgotado no estoque.')
                
                break
        if not livro_encontrado:
            print('Número não válido, tente novamente.')
        novo_arq=open(arq, 'wt')
        novo_arq.writelines(linhas_do_arq)
        novo_arq.close