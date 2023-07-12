'''
>> WHILE

Usado para repetir um bloco de codigos várias vezes. Faz sentido usar while quando NÃO SABEMOS
o número exato de vezes que nosso bloco de código deve ser executado.

'''

# Exemplo 1
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato\n[3] Sair \nDigite a opcao: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Emitindo extrado..")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")