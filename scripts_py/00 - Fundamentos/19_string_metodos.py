'''
EXEMPLOS DE ALGUNS MÉTODOS DE STRINGS

'''

curso = "pYtHon"
print(curso.upper())    # Tudo maiúsculo    
print(curso.lower())    # Tudo minúsculo
print(curso.title())    # Primeira letra maiúscula

# >> ELIMINANDO ESPAÇOS EM BRANCO

curso = "   Python "    # reparar no espaço antes e depois da palavra Python
print(curso.strip())    # remove TODOS os espaços em branco
print(curso.lstrip())   # remove os espaços à esquerda
print(curso.rsplit())   # remove os espaços à direita

# >> INSERINDO CARACTERES 

curso = "Python"
print(curso.center(10, "#"))    # Centraliza o texto inserindo caracteres até totalizar o número indicado
print(".".join(curso))          # Insere o caracter selecionado entre cada ITERÁVEL da variável


# alternativa ao uso do join usando for
for letra in curso:
    print(curso, end=".")       # Percorre cada letra da variável e insere o "." entre cada letra.
print()