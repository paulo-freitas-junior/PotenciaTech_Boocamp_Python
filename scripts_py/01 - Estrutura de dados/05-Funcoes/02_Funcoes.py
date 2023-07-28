'''
Parâmetros Especiais de Funções

Para uma melhor legibilidade e desempenho, restringir a maneira como os argumentos são passados.

Passados:
    >> por posição
    >> por posição e nome
    >> por nome

Syntax:
=======

def funcao(pos1, pos2, /, pos_ou_nome, *, nome1, nome2):
           ----------     -----------     ------------
            |               |                   |
            |           posicao ou nome         |
            |                               nome apenas
        Posicao apenas
'''

# POR POSIÇÃO APENAS - Positional Only
#===================================

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')   # Válido conforme Syntax


# POR NOME APENAS - Keyword Only
#===============================

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')  # Válido


# POR NOME E POSIÇÃO APENAS - Keyword and positional only
#========================================================

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')   # Válido


'''
OBJETOS DE PRIMEIRA CLASSE
==========================

Em Python tudo é objeto, dessa forma as FUNÇÕES TAMBÉM SÃO OBJETOS, o que as tornam objetos de primeira classe.
É possível atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em 
estruturas de dados (listas, tuplas, dicinários, etc) e usar como valor de retorno para uma função (closures).
'''

def somar(a, b):
    return (a + b)

def subtrair(a, b):
    return (a - b)

def multiplicar(a, b):
    return (a * b)


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é {resultado}')

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, multiplicar) # O resultado da operação 10 * 10 = 100


# Atribuindo apontamentos das variáveis de função

op_soma = somar    # atribuindo à variável OP_SOMA a função SOMAR
print(op_soma(10,20))

op_subtrai = subtrair
print(op_subtrai(50, 20))

#---


'''
ESCOPO LOCAL E ESCOPO GLOBAL
============================
Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali
feitas em OBJETOS IMUTÁVEIS serão perdidas quando o método terminar de ser executado. Para usar objetos globais
é utilizado a palavra-chave GLOBAL, que informa ao interpretador que a variável que está sendo manipulada no
escopo local é global.

OBS: NÃO É UMA BOA PRÁTICA E DEVE SER EVITADO!
'''

salario = 2000  # variável de escopo GLOBAL pois está fora do bloco da função (raiz do programa)

def salario_bonus(bonus):
    global salario          # necessario 
    salario += bonus
    return salario

salario_bonificado = salario_bonus(500)  # retorna soma salario + bonus (2000 + 500) = 2500
print(salario_bonificado)

