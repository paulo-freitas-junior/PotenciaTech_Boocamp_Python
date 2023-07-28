'''
Definição - OPERADORES LÓGICOS
São operadores utilizados em conjunto com os operadores de comparação, para montar uma 
expressão lógica. Quando um operador de comparação é utilizado, o resuldado retornado é
um booleano, dessa forma podemos combinar operadores de comparação com os operadores
lógicos, exemplo:

op_comparacao + op_logico + op_comparacao.... N ....

'''

# AND = para ser True, TUDO tem que ser True
# OR = para ser True, APENAS um tem que ser True

print(f"True AND True =", True and True)
print(f"True AND False =", True and False)
print(f"False AND False =", False and False)
print(f"True OR True =", True or False)
print(f"False OR False =", True or True)

saldo = 1000
saque = 200
limite = 100

# operador AND todas as partes precisam ser verdadeiras para True ou falsas para False
print(saldo >= saque and saque <= limite)   # Caso aqui é False - uma lógica é falsa

# operador OR - Uma condição precisa ser verdadeira para ser True a expressão
# Ou uma falsa para False
print(saldo >= saque or saque <= limite)   # Uma condição  aqui é verdadeira

# operador NOT
contatos_emergencia = []

# 1000 não é maior que 1500, mas com o NOT na frente se torna False
print(not 1000 > 1500)  

# Uma sequencia VAZIA em python é considerada False, mas com NOT se torna True
print(not contatos_emergencia)

# Uma String possui dados/valores, mas com NOT ela se forna False
print(not "saque 1500;")

# String vazia é Falso. com o NOT se torna True
print(not "")


# PARÊNTESES DELIMITANDO PRECEDÊNCIA NOS OPERADORES LÓGICOS
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <=limite or conta_especial and saldo >= saque
exp2 =(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp1)
print(exp2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)