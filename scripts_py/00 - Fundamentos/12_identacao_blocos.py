'''
Identar código é uma forma de manter o código fonte mais legível e manitenível.
Python a indentação é necessária para o interpretador determinar onde o bloco de 
comando inicia e onde ele termina.

Bloco de comando - As linguagens de programação costumam utilizar caracteres ou
palavras reservadas para terminar o início e o fim do bloco. Nas linguagens Java
e C por exemplo, utilizamos chaves:

Python - Por convenção usa-se 4 espaços em branco para cada nível de indentação

'''

saldo = 500.00

def sacar(valor):
    if saldo >= valor:
        print("valor sacado.")
        print("Retire o seu dinheiro na boca do caixa")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo += valor

sacar(100)