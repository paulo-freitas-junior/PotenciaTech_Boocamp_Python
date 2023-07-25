'''
Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros,
esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível
e possibilita o reaproveitamento de código. 
Programar baseado em funções é o mesmo que dizer que está programando de forma estruturada.

'''
# Sem passagem de parâmetros
def exibir_mensagem():
    print('Olá mundo!')

# Passando parâmetros para RECEBER um dado
def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}!')

# Passando parâmetros para RECEBER um dado, porém com um DADO definido caso não seja informado
def exibir_mensagem_3(nome="Anônimo"):
    print(f'Seja bem vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2(nome="Paulo") # Passando argumentos
exibir_mensagem_2("Sharon")

exibir_mensagem_3()
exibir_mensagem_3(nome="Elaine")
exibir_mensagem_3("Luna")



# RETORNANDO VALORES
# ==================
'''
Para retornar um valor é usado a palavra reservada RETURN.
Toda função Python retorna NONE, por padrão. 
'''

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

calcular_total([10, 20,34])
retorna_antecessor_e_sucessor(10)


# ARGUMENTOS NOMEADOS
# ===================
'''
Chamamos de Chave=Valor
'''

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat','Palio',1999,'ABC-1234')    # método 1 - passando parámetros na ORDEM CORRETA!
salvar_carro(marca='Fiat',modelo='Palio',ano=1999,placa='ABC-1234') # método 2 - definindo argumentos NOMEADOS
salvar_carro(**{'marca':'Fiat', 'modelo':'Palio', 'ano':1999, 'placa':'ABC-1234'})  # método 3 - inserindo por CHAVE/VALOR


# ARGS E KWARGS
# =============
'''
Combinar parâmetros obrigatórios com args e kwargs.
*args = método recebe os valores como uma TUPLA (TUPLE)
*kwargs = método recebe ops valores como um DICIONÁRIO (DICT)

'''
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}:{valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema(',Segunda, 25 de Setembro de 2023','Zen of Pyhon', 'Beatiful is better than ugly.', autor='Tim Peters', ano=1999)
