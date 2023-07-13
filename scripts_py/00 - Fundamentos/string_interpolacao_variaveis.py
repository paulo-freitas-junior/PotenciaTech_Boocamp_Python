'''
INTERPOLAÇÃO DE VARIÁVEIS
Existem 3 formas:

1 - usando o sinal %  - NÃO É RECOMENDADO.
2 - usando o método format
3 - usando f strings - MAIS RECOMENDADO.

'''

# MÉTODO ANTIGO USANDO %
#-----------------------
nome = "Paulo"
idade = 46
profissao = "Cientista"
linguagem = "Python"

# Sendo:
# s% >> Strings
# %d >> Inteiros
# f% >> Float

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


# MÉTODO USANDO FORMAT
#---------------------
nome = "Paulo"
idade = 46
profissao = "Cientista"
linguagem = "Python"
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))


# usando recursos de indexação por ordem. (Posição da variável).   Base 0 inicial do índice.
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))


# usando recursos de identificação com variáveis
print("Olá, me chamo {name}. Eu tenho {age} anos de idade, trabalho como {job} e estou matriculado no curso de {course}.".format(
    name = nome,
    age = idade,
    job = profissao,
    course = linguagem))


# usando DICIONÁRIOS do Python 
dados ={"nome": "Paulo", "idade": 46, "profissao": "Cientista", "linguagem": "Python"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))


# MÉTODO USANDO F STRING  - MELHOR MANEIRA !!
#----------------------------------------------------
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


# FORMATAÇÃO ADICIONAL
# ----------------------
PI = 3.14159    # constante
print(f"Valor de PI: {PI:2f}")      # Definindo 2 casas decimais
print(f"Valor de PI: {PI:10.2f}")   # Insere 10 ESPAÇOS em branco no início
