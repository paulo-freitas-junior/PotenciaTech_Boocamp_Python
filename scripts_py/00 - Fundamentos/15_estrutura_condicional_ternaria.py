'''
IF TERNÁRIO

Permite escrever uma condição em uma única linha. Ele é composto por três partes,
a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a 
expressão lógica e a terceira parte é o retorno caso a expressao não seja atendida.

'''

saldo = 1000.0
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
