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
    