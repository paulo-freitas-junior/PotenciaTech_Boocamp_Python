'''
DESAFIO
=======

Deixar a versão 1 do código de Desafio Bancário mais modularizado, para isso criando funções para as operações
existentes: sacar, depositar e visualiar histórico. Criar duas novas funções: criar usuário (cliente do banco)
e criar conta corrente (vincular com usuário).

>> SEPARAÇÃO DAS FUNÇÕES:

Criar funções para todas as operações do sistema. Cada função terá uma regra na PASSAGEM DE ARGUMENTOS 
(opção POR POSIÇÃO e opção NOMEADOS).
O retorno e a forma como serão chamadas, podem ser definidas conforme critérios do programador.

>> SAQUE
--------
    Deve receber os argumentos apenas por nome (keyword only).
    Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
    Sugestão de retorno: saldo e extrato.

>> DEPÓSITO
-----------
    Deve receber os argumentos apenas por posição (positional only).
    Sugestão de argumentos: saldo, valor, extrato.
    Sugestão de retorno: saldo e extrato.

>> EXTRATO
----------
    Deve receber os argumentos por posição e nome (positional only e keyword only)
    Argumentos posicionais: saldo.
    Argumentos nomeados: extrato.


>> NOVAS FUNÇÕES:

Criar duas novas funções: CRIAR USUÁRIO e CRIAR NOVA CONTA CORRENTE.

>> CRIAR USUÁRIO (CLIENTE)

    O programa deve armazenar os usuários em uma LISTA, um usuário e composto por:
    nome, data de nascimento, cpf e endereço. O endereço é uma STRING com formato:
    logradouro, nº - bairro - cidade/sigla do estado. Deve ser armazenado somente os 
    números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

>> CRIAR CONTA CORRENTE

    Sistema deve armazenar contas em uma LISTA. Uma conta é composta por: agência,
    número da conta e usuário. 
    O número da conta é SEQUENCIAL, iniciando em 1.
    O número da agência é fixo: "0001". 
    O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    

OBS: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número
do CPF, informado para cada usuário da lista.

'''

import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar novo usuário
    [5]\tCriar nova conta corrente
    [6]\tListar contas cadastradas
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):    # argumentos positional only
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # argumentos kwyword only
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o valor limite para saque. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques permitidos excedidos. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):   # argumentos keyword only e positional only
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


# Funções de criação de Usuário e Conta Corrente

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário cadastrado com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, criação de conta encerrada! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor para depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input("Informe o valor para saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# executando a função main() do sistema

main()