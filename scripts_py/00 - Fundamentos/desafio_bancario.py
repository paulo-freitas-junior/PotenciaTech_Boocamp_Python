'''
Desafio - Criando um Sistema Bancário com Python

>> OBJETIVO
Criar um sistema bancário com as operações: sacar, depositar, visualiar extrato.
================================================================================

Implementar 3 operações: depósito, saque, extrato.

>> OPERAÇÃO DE DEPÓSITO
-----------------------

Deve ser possível depositar valores POSITIVOS para uma conta bancária. A Versão 1 do projeto
trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual 
é o número da agência e conta bancária. Todos os depósitos dever ser armazenados em uma 
VARIÁVEL e exibidos na operação extrato.


>> OPERAÇÃO DE SAQUE
---------------------

O sistema deve permitir realizar 3 SAQUES DIÁRIOS com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não
será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma 
VARIÁVEL e exibidos na operação extrato.

>> OPERAÇÃO DE EXTRATO
----------------------

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve
ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxxx.xx, exemplo: R$ 1500.00

'''

#  criando o menu de opções

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

# definindo as variáveis e constantes

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# estrutura de decisões e execução

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))

        if valor >= 0:
            saldo += valor  # adiciona valor de depósito no saldo
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação inválida. Valor informádo inválido.")

    elif opcao == 's':
        valor = float(input('Digite o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida. Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação inválida. Você não possui limite para o saque solicitado.")

        elif excedeu_saques:
            print("Operação inválida. Número máximo de saques excedido no sistema.")

        elif valor > 0:
            saldo -= valor  # debita do saldo o valor do saque solicitado
            extrato += f'Saque: R$ {valor:.2f}\n'  # debita do extrato o valor do saque mostrando o valor sacado
            numero_saques +=1   # contador de saques

    elif opcao == 'e':
        print("\n========== EXTRATO BANCÁRIO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 'q':
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")