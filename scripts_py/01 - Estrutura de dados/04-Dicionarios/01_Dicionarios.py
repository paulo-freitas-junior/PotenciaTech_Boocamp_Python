'''
Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas e em
uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista
de pares chave:valor separada por vírgulas.

'''
# Formas de criar um dicionário
# dicionario = {'chave:valor','chave:valor'.....}
# dicionario = dict(chave='valor', chave='valor', chave=valor, .....)

pessoa = {"nome":"Paulo", "idade":46}   # declaração 
pessoa = dict(nome="Ze Mane", idade=88) # via uso do dict


# Add nova chave:valor ao dicionário pessoa
# dicionario['chave'] = 'valor'

pessoa["telefone'"] = "3333-1234"
print(pessoa)


# Acessando os dados do dicionário através das CHAVES
# dicionario['chave']

dados = {'nome':'Paulo', 'idade':46, 'telefone': '91234-1234'}

print(dados)
print(f'Nome:', dados['nome'])
print(f'Idade:', dados['idade'])
print(f'Telefone:', dados['telefone'])


# Alterando o VALOR das chaves de um dicionário
# dicionario['chave'] = 'valor'

dados['nome'] = "Elaine"
dados['idade'] = 43
dados['telefone'] = '98793-9873'

print(dados)


'''
DICIONÁRIOS ANINHADOS
=====================
Podem armazenar qualquer tipo de objeto Python como VALOR, desde que a CHAVE para esse valor
seja um objeto imutável como (strings e números).

Estrutura muito parecida com Banco de Dados

'''

# String : {dicionarios}

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}

# acessando a CHAVE (string) e retornando o resultado da CHAVE selecionada
print(contatos['zemane@gmail.com']['telefone']) # '3333-2222'

'''
ITERAR DICIONÁRIOS
==================

A forma mais comum para percorer os dados de um dicionário é utilizando o comando FOR.

'''

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}

# Opção 1 - Não muito usada
for chave in contatos:
    print(chave, contatos[chave])

# Opção 2 - Mais usada
for chave, valor in contatos.items():
    print(chave,valor)
    