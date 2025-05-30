def cabecalho(t):
    print('_'*30)
    print(f'{t:^30}')
    print('_'*30)


def color(a):
    if a == 'a':
        return '\033[33m'
    if a == 'v':
        return '\033[31m'
    if a == 'az':
        return '\033[34m'
    if a == '':
        return '\033[m'


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont=0
    for item in lista:
        cont+=1
        print(color('a'),f'{cont} - ',color('az'),f'{item}',color(''))
