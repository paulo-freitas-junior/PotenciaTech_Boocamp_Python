'''
MÉTODOS APLICADOS A LISTAS

'''

# ADICIONANDO ITENS NA LISTA
# [].append()

lista = []
lista.append(1)
lista.append('Paulo')
lista.append([40, 30, 20])      # inserindo uma lista DENTRO da lista
print(lista)


# LIMPANDO OS DADOS DE UMA LISTA
# [].clear()

lista = [1, 'Paulo', [40, 30 ,20]]
print(lista)
lista.clear()       # limpa os dados da lista
print(lista)


# COPIAR OS DADOS DE UMA LISTA EN UMA INSTÂNCIA DIFERENTE
# [].copy()

lista = [1, 'Paulo', [40, 30 ,20]]
lista2 = lista.copy()
lista2[0] = 'Python'        # altera primeiro objeto da lista2
print(lista)
print(lista2)


# CONTAR QUANTAS VEZES UM DETERMINADO OBJETO EXISTE DENTRO DA LISTA
# [].count()

cores =['vermelho','azul','verde','azul']
print(f'total de cores vermelhas: ', cores.count('vermelho'))
print(f'total de cores verdes: ', cores.count('verde'))
print(f'total de cores azul: ', cores.count('azul'))


# FAZ UM MERGE DE UMA LISTA PARA OUTRA
# [].extend()

linguagens = ['python', 'js', 'c']
print(linguagens)
linguagens.extend(['java','csharhp'])       # junta nova lista de elementos na lista definida
print(linguagens)


# LOCALIZAR A PRIMEIRA OCORRENCIA DE UM OBJETO NA LISTA
# [].index()

linguagens = ['python','js','c','java','csharp','js']
print(linguagens.index('python'))
print(linguagens.index('js'))      # apresenta APENAS a primeira ocorrência d para 'js'  - caso índice 1
print(linguagens.index('csharp'))


# REMOVER OBJETOS DE UMA LISTA ATRAVÉS DO ÍNDICE - sem valor de índice, remove sempre pela última
# [].pop()

linguagens = ['python','js','c','java','csharp','js']
print(f'Linguagem a ser removida: ', linguagens.pop(), f' - Novo valor da lista: ', linguagens)  # [5] = js
print(f'Linguagem a ser removida: ', linguagens.pop(), f' - Novo valor da lista: ', linguagens)  # [4] = csharp
print(f'Linguagem a ser removida: ', linguagens.pop(), f' - Novo valor da lista: ', linguagens)  # [3] = c
print(f'Removendo a linguagem do índice [0]: ', linguagens.pop(0))                               # [0] = python
print(f'Itens sobrando na lista: ', linguagens)


# REMOVE OBJETOS DE UMA LISTA IDENTIFICANDO O OBJETO A SER REMOVIDO
#[].remove()

linguagens = ['python','js','c','java','csharp','js']
linguagens.remove('js')      # OBS: remove o PRIMEIRO objeto caso exista mais de um igual na lista
print(linguagens)


# INVERTE A ORDEM DA LISTA 
# [].reverse()

linguagens = ['python','js','c','java','csharp','js']
print(f'Ordem original da lista: ', linguagens)
linguagens.reverse()    # inverte a ordem da Lista
print(f'Ordem inversa da Lista: ', linguagens)


# ORDENAÇÃO DE LISTAS
# [].sort()

linguagens = ['python','js','c','java','csharp','js']
print(f'Ordem original da lista: ', linguagens)
linguagens.sort()                                   # ordena a lista em ordem alfabética ou numérica
print(linguagens)

linguagens = ['python','js','c','java','csharp','js']
print(f'Ordem original da lista: ', linguagens)
linguagens.sort(reverse=True)                       # ordena a lista alfabeticamente invertida
print(linguagens)

linguagens = ['python','js','c','java','csharp','js']
print(f'Ordem original da lista: ', linguagens)
linguagens.sort(key=lambda x: len(x))               #ordena CRESCENTE pela quantidade de letras (tamanho da string) de cada item da lista 
print(linguagens)

linguagens = ['python','js','c','java','csharp','js']
print(f'Ordem original da lista: ', linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True) #ordena DECRESCENTE pela quantidade de letras (tamanho da string) de cada item da lista 
print(linguagens)


# IDENTIFICA A QUANTIDADE DE ELEMENTOS DENTRO DA LISTA
# [].len() - função de Lista

linguagens = ['python','js','c','java','csharp','js']
print(linguagens)
print(f'Quantidade de elementos da lista: ', len(linguagens))


# ORDENAÇÃO DE LISTAS 
# [].sorted() - função built-in do Python

linguagens = ['python','js','c','java','csharp','js']
print(f'Lista sortida por tamanho opção 1: ', sorted(linguagens))  
print(f'Lista sortida por tamanho opção 2: ', sorted(linguagens, key=lambda x: len(x)))
print(f'Lista sortida por tamanho reverso: ', sorted(linguagens, key=lambda x: len(x), reverse=True))