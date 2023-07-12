'''
IF ANINHADO

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar
estruturas IF/ELIF/ELSE dentro do bloco de código de estruturas IF/ELIF/ELSE.

'''
conta_normal = True             # experimente trocar
conta_universitaria = False     # experimente trocar

saldo = 2000.0
cheque_especial = 450

saque = float(input("Informe valor do saque: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
        
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema naão reconehceu seu tipo de conta. Entre em contato com gerente")