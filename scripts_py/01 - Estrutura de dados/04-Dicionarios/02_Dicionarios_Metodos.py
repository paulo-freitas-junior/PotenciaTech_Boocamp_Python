'''
MÉTODOS DOS DICIONARIOS (DICT)
'''

# LIMPAR O DICIONÁRIO - Limpa TODOS os objetos do dicionário
# {}.clear()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}

contatos.clear()
print(contatos)


# COPIANDO UM DICIONÁRIO
# {}.copy()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'}
}

copia = contatos.copy()     # criando uma cópia em novo dicionário
copia['zemane@gmail.com'] = {'nome:': 'Zezinho Mane'}   # alterando valor da chave nome para String do DICT

print(contatos['zemane@gmail.com'])
print(copia['zemane@gmail.com'])


# Cria NOVAS CHAVES no Dicionário
# {}.fromkeys()

dict.fromkeys(['nome', 'telefone'])     # CRIANDO CHAVES SEM VALOR - {'nome': None, 'telefone': None}
dict.fromkeys(['nome', 'telefone'], 'vazio')    # CRIANDO CHAVES COM VALOR PADRÃO - {'nome': 'vazio', 'telefone': 'vazio'}


# Acessar VALORES dentro do dicionário
# {}.get()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'}
}

print(contatos.get('chave'))                        # KeyError - Não existe chave com esse nome
print(contatos.get('chave', {'Não localizado'}))     # Não localizando retorna mensagem definida como padrão
print(contatos.get('zemane@gmail.com', {}))         # Retorna os dados da chave


# Retorna uma lista - Útil no comando FOR para interar
# {}.items()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'}
}

print(contatos.items())


# Retorna APENAS AS CHAVES do dicionário
# {}.keys()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze mane das Coves', 'telefone-': '4444-3333'}
}

print(contatos.keys())


# Remover uma CHAVE do dicionário
# {}.pop()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze mane das Coves', 'telefone-': '4444-3333'}
}

resultado = contatos.pop('zemane@gmail.com')    # remove a chave definida e mostra o resultado da remoção
print(resultado)                                # mostra resultado como {}

resultado = contatos.pop('zemane@gmail.com', {'Chave informada não encontrada'})   # mostra resultado com mensagem definida.
print(resultado)


# Remove 
# {}.popitem()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze mane das Coves', 'telefone-': '4444-3333'}
}

resultado = contatos.popitem()
print(resultado)                # mostra resultado removido      
# print(contatos.popitem())       # gera um KeyError devido item ter sido removido no comando acima


# Adiciona um conjunto CHAVE/VALOR no dicionário com um valor sendo default definido
# {}.setdefault()

contato = {'nome': 'Paulo', 'telefone': '3333-2222'
}

contato.setdefault('nome', 'Elaine')    # não adiciona SE O ATRIBUTO JÁ EXISTIR NO DICIONÁRIO (chave 'nome' já existe)
print(contato)

contato.setdefault('idade', 46)         # adiciona no dicionário chave/valor definida que não existe no dicionário
print(contato)


# Faz um UPDATE no dicionário ALTERANDO valores de uma chave ou INSERINDO novos elementos no Dicionário
# {}.update()

contatos = {'zemane@gmail.com': {'nome': 'Zezão', 'telefone': '3333-1111'}
}

# >> alterando 
contatos.update({'zemane@gmail.com': {'nome': 'Zezinho'}})  # Altera o nome para Zezinho na chave definida 'zemane@gmail.com'

# >> criando novo dicionario
contatos.update({'zezao@gmail.com': {'nome': 'Zezao', 'telefone': '1234-5678'}}) # Update no dicionário add novos registros
print(contatos)


# Retorna apenas os VALORES (dicionarios) sem as chaves.
# {}.values.()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}
resultado = contatos.values()
print(resultado)


# Verifica se um determinado VALOR se encontra dentro de uma CHAVE
# {}.in()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}

resultado = 'zemane@gmail.com' in contatos      # True
print(resultado)

resultado = 'joaopedefeijao@gmail.com' in contatos      #False
print(resultado)

resultado = 'idade' in contatos['zemane@gmail.com']     # False
print(resultado)

resultado = 'telefone' in contatos['fulana1@gmail.com'] # True
print(resultado)


# Deleta o OBJETO que se deseja remover dentro do DICIONARIO
# {}.del()

contatos = {
    'zemane@gmail.com': {'nome': 'Ze Mane', 'telefone': '3333-2222'},
    'zezinho@gmail.com': {'nome': 'Zezinho', 'telefone': '2222-1111'},
    'fulana1@gmail.com': {'nome': 'Fulaninha', 'telefone': '1111-0000'},
}

del contatos['zemane@gmail.com']['telefone']        # remove apenas a chave de telefone no dicionario definido
del contatos['fulana1@gmail.com']                   # remove todos objetos do dicionário definido pela chave
