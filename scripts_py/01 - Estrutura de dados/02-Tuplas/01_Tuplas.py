'''
TUPLAS
São estruturas de dados muito parecidas com as listas, as tuplas não são mutáveis.
pode ser criada através da classe TUPLE, ou colocando valores separados por vírgula
de parenteses.

'''

frutas = ('laranja','pera','uva',)   # uso de PARENTESES - ATENCAO AO USO DE VIRGULA NO FINAL!!!

letras = tuple('python')

numeros = tuple([1, 2, 3, 4, 5])    # inserindo uma lista dentro de uma tupla. NÃO É POSSIVEL ALTERAR

pais =('Brasil',)   # atenção ao uso da vírgula no final!!


# >> Acessando valores da tupla pelos índices
frutas =('mação',' laranja','uva','pera',)
print(frutas[0])
print(frutas[2])


# >> Acessando índices negativos
print(frutas[-1])
print(frutas[-3])


'''
TUPLAS podem armazenar outros tipos de objets Python.
Tuplas podem armazenar outras tuplas, criando estruturas bidimensionais (tabelas),
e acessar informações através dos índices de linha e coluna.
'''
matriz =(
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c',),    
)

print(matriz[0])        # (1,'a',2)
print(matriz[0][0])     # 1
print(matriz[0][-1])    # 2
print(matriz[-1][-1])   # 'c'


# >> FATIAMENTO - SLICE
# (start:stop:step)
tupla = ('p','y','t','h','o','n',)
print(tupla[2:])        # ('t','h','o','n)
print(tupla[:2])        # ('p','y')
print(tupla[1:3])       # ('y',t')
print(tupla[::])        # ('p','y','t','h','o','n')
print(tupla[::-1])      # ('n',o',h',t',y',p')


# Interação com FOR
carros = ('gol1','celta','palio',)

for carro in carros:
    print(carro)


# Acessando índices na Tupla usando FOR
carros = ('gol1','celta','palio',)

for indice, carro in enumerate(carros):
    print(f'{indice},{carro}')
