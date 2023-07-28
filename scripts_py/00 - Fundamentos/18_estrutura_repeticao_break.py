# USANDO BREAK COM WHILE
# ----------------------
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    print(numero)
    print("Teste realizado usando o While + Break")    


# USANDO BREAK + CONTINUE COM WHILE
# ----------------------------------

while True:
    numero = int(input("Informe o número: "))

    if numero == 10:
        break

    if numero %2 == 0:
        print(numero)


# USANDO BREAK COM FOR
#----------------------
for numero in range(100):

    if numero == 10:        # exibe de 0 a 9
        break               # irá PARAR a contagem no número definido
    print(numero, end=" ")
print("\nTeste realizado com FOR + Break")      # \n insere o texto na linha abaixo


# USANDO CONTINUE COM FOR
#----------------------
# EXEMPLO - Exibindo os números ímpares
for numero in range(100):

    if numero %2 == 0:      # MOD - impressao dos números ímpares
        continue
    print(numero, end=" ")