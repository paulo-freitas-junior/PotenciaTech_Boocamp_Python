'''
CONJUNTOS - SET

é um SET (coleção) que não possui objetos repetidos, usamos sets para representar conjuntos
matemáticos ou eliminar itens duplicados de um iterável.

Ele ELIMINA OS ITENS DUPLICADOS de uma LISTA!!
Obs: Em Strings a ordem de resultados é randômica.
'''

numeros = set([1,2,3,1,3,4])    # Criando um set com uma Lista de elementos (1,2,3,4)
print(numeros)

fruta = set('abacaxi')          # (inserindo um iterário)
print(fruta)

carros = set(('palio','gol','celta','palio'))   # Criando um Set usando uma Tupla de elementos
print(carros)

linguagens = {'python','java','python'}         # Estrutura do SET
print(linguagens)


'''
Conjuntos Python não suportam indexação (index) e nem fatiamento (slice).
Necessário converter o SET para uma LIST!!!!!
'''

numeros = {1,2,3,2}        # set{}
numeros = list(numeros)    # convertendo para lista     
print(numeros[0])          # acessando o índex da lista


# >> Percorrendo os DADOS de um conjunto (SET) é usando o comando FOR
carros ={'gol','celta','palio'}
for carro in carros:
    print(carro)


# >> Percorrendo os ÍNDICES de um conjunto (SET)
carros ={'gol','celta','palio'}
for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')


# MÉTODOS DA CLASSE SET
#=======================

# União de Conjuntos
# [].union()

conjunto_a = {1,2}
conjunto_b = {3,4}

uniao = conjunto_a.union(conjunto_b)    # {1,2,3,4}
print(uniao)


# Intersecção de Conjuntos
# [].intersection()

conjunto_c = {1,2,3}
conjunto_d = {2,3,4}

interseccao = conjunto_c.intersection(conjunto_d)   # {2,3}
print(interseccao)


# Diferença de Conjuntos
# [].difference

conjunto_e = {1,2,3}
conjunto_f = {2,3,4}

diferenca1 = conjunto_e.difference(conjunto_f)   # {1}
diferenca2 = conjunto_f.difference(conjunto_e)   # {4}
print(diferenca1)
print(diferenca2)


# Diferença Simétrica de Conjuntos  - Dados que não estão na intersecção
# [].symmetric_difference()

conjunto_g = {1,2,3}
conjunto_h = {2,3,4}

diff_simetrica = conjunto_g.symmetric_difference(conjunto_h)
print(diff_simetrica)


# 
# [].issubset()

conjunto_i = {1,2,3}
conjunto_j = {4,1,2,5,6,3}

subset1 = conjunto_i.issubset(conjunto_j)    # True - Elementos de I pertencendo a J
subset2 = conjunto_j.issubset(conjunto_i)    # False - Elementos de J não pertencem TODOS a i
print(subset1)
print(subset2)


# Verifica se um elemento de um Conjunto está inserido em outro Conjunto 
# [].isdisjoint()

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

resp1 = conjunto_a.isdisjoint(conjunto_b)       # True  - não existe intersecção
resp2 = conjunto_a.isdisjoint(conjunto_c)       # False  - existe intersecção
print(resp1)
print(resp2)

# Adicionando elementos ao SET
# [].add()

sorteio = {1,23}

sorteio.add(25)     # {1,23,25}
sorteio.add(42)     # {1,23,25,42}
sorteio.add(25)    # {1,23,25,42}      # NÃO ADICIONA POR JÁ EXISTE UM ELEMENTO IGUAL !!!!!
print(sorteio)


# Limpando dados de um Conjunto
# [].clear()

sorteio = {1,23}

sorteio.clear()
print(sorteio)  # {}


# Copiando dados de um Conjunto
# [].copy()

sorteio = {1,23}
sorteio.copy()
print(sorteio)


# Eliminando valores duplicados no SET
# [].discard()

numeros ={1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.discard(1)      # discarta todos os elementos de numero 1
print(numeros)

numeros.discard(45)     # discarta elementos de número 45 (se houver...)
print(numeros)


# REMOVE OS PRIMEIROS VALORES DA LISTA  - OBS!
# [].pop()

numeros ={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)      # não imprime os elementos duplicados. Imprime em ordem.
print(numeros.pop())    # 0
print(numeros.pop())    # 1
print(numeros)

# Remove APENAS os elementos existentes dentro do SET.
# [].remove()

numeros ={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros.remove(0))    # remove o 0
# print(numeros.remove(45))    # Gera um ERRO se não houver o elemento no SET
print(numeros)


# Contando a quantidade de elementos no Conjunto
# [].len()

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
len(numeros)


# Verificando Objetos dentro de um SET
# [].in()

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
1 in numeros    # True
10 in numeros   # False

