#MERGE SORT:

def mergesort (lista, inicio=0, fim=0):
    if fim == 0:
        fim = len(lista)
    if (fim - inicio)>1:
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return None

def merge (lista, inicio, meio, fim):
    listaEsquerda = lista[inicio:meio]
    listaDireita = lista[meio:fim]
    topoE = 0
    topoD = 0

    for k in range(inicio, fim):
        if topoE >= len(listaEsquerda):
            lista[k] = listaDireita[topoD]
            topoD = topoD + 1
        elif topoD >= len(listaDireita):
            lista[k] = listaEsquerda[topoE]
            topoE = topoE + 1
        elif listaEsquerda[topoE] < listaDireita[topoD]:
            lista[k] = listaEsquerda[topoE]
            topoE = topoE +1
        else:
            lista[k] = listaDireita[topoD]
            topoD = topoD + 1
    return None

#FATORIAL:

def fatorial(n=1):
    '''
    Função Fatorial
    :para número inteiro ser fatorado
    :return caso certo retorna reultado, se der erro -1
    '''
    try:
        n = int(n)
        fat = 1
        for i in range(1, n + 1):
            fat = i * fat
        print("O fatorial de", n, "é: ", fat)
        return fat

    except:
        print("---" * 30)
        print("{:^90}".format("-1"))
        print("O valor digitado não pode ser fatorado.")
        print("---" * 30)
        return -1

#JOGAR DADOS:

def rolarDado(qDado=1):
    '''
    Função para jogar dados:
    :param qDado: A quatidade de dados à serem jogados
    :return: O resultado de cada dado
    '''
    from random import randint
    rDado = []
    for i in range(qDado):
        rDado.append(randint(1,6))
    return rDado