'''
LISTAS

Armazenar de maneira sequencial qualquer tipo de objeto. Possível criar listas utilizando
o construtor LIST, a função RANGE ou colocando valores separados por vírgula dentro de
colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a
criação.

A lista é uma sequência, portanto o acesso aos dados é via ÍNDICE, iniciando sempre em [0]

'''

# EXEMPLOS DE LISTAS

# >> declaradas com ou sem objetos
frutas = []     # declaração de uma Lista vazia em uma variável
frutas = ['laranja','maca','uva', 'pera']       # Lista declarada na variável com objetos

# >> utilizando método list
letras = list['PAULO']        # CADA LETRA da palavra é um ITEM da Lista !!
numeros = list(range(10))       # Cria uma variável com um lista numérica de 0-9

# >> declarando com tipos de objetos diferentes
carro =['Ferrari','F8', 42000000, 2020, 2900, 'São Paulo', True]

# VISUALIZANDO

print(frutas[0])    # maçã
print(frutas[2])    # uva

''' Sequências suportam indexação negativa. A contagem começa em -1 '''
print(frutas[-1])   # pera
print(frutas[-3])   # laranja


'''
LISTAS ANINHADAS - REPRESENTAÇÃO DE MATRIZ BIDIMENCIONAL

Listas podem armazenar todos os tipos de objetos Python, inclusive uma lista pode 
armazenar outra lista criando estruturas bidimensionais (TABELAS), e acessar informando
os índices de linha e coluna. 

'''
# >> MATRIZ 3x3 - 3 Linhas e 3 colunas
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])       # [1,'a',2] >> Acessa dados da primeira LINHA
print(matriz[0][0])    # 1         >> acessa dado da Linha 1 e Coluna 1
print(matriz[0][-1])   # 2         >> acessa dado da Linha 1 e Coluna -1 (indexação negativa)
print(matriz[-1][-1])  # 'c'       >> acessa dado da Linha -1 e Coluna -1 (indexação negativa)
print(matriz[-2][-2])  # 3         >>

'''
FATIAMENTO DE LISTAS

Extrair o conjunto de valores de uma sequência, acessando o índice inicial e/ou final
para acessar o conjunto, podendo inclusive informar quantas posições o cursos deve
"pular" o acesso.

Lista = [start:stop:step]
'''
lista = ['p', 'y', 't', 'h', 'o', 'n']      # 06 elementos na lista

print(lista[2:])        # ['t','h','o','n']
print(lista[:2])        # ['p','y']
print(lista[1:3])       # ['y,'t']
print(lista[0:3:2])     # ['p','t']
print(lista[::])        # ['p','t','h','o','n']
print(lista[::-1])      # ['n','o',h',t','y','p']

'''
ITERAR LISTAS
Percorrer uma lista utilizando o comando FOR
'''
carros =['gol', 'celta','palio']
for carro in carros:
    print(carro)


'''
FUNÇÃO ENUMERATE
Identificar qual ÍNDICE do objeto está dentro de um laço FOR.

Syntax:

lista =[]

for índice, variável in enumerate(lista):
    print(f'{indice} : {variável})

'''

carros =['gol', 'celta','palio']
for indice, carro in enumerate(carros):
    print(f'{indice} : {carro}')


'''
COMPREENSÃO DE LISTAS
Oferece uma sintaxe mais curta permitindo:
1- criar uma nova lista com base nos valores de uma lista existente(filtro).
2- gerar uma nova lista aplicando alguma modificação nos elementos de uma
   lista existente.

OPÇÃO 1 - Syntax:
=================

lista_dados = [1,2,3,4]        # lista com os dados
lista_recebe = []              # lista que recebe dados da lista_dados

for variável in lista_dados:
    if variável % 2 == 0:
        lista_recebe.append(variável)   # adiciona novos valores conforme IF
'''

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)        # adicionando objetos pares da condicao IF na variável pares


# >> modificando valores
#-----------------------
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero ** 2)   # elevando ao quadrado o valor da variável

'''
OPÇÃO 2 - Syntax:
=================

lista_dados = [1,30,21,2,9,65,34]
lista_recebe = [variável for variável in lista_dados if variável 'CONDIÇÃO']
'''

numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# >> modificando valores
#-----------------------
numeros = [1,30,21,2,9,65,34]
pares = [numero ** 2 for numero in numeros if numero % 2 == 0]    # primeira variável recebe valor elevado ao quadrado
print(pares)