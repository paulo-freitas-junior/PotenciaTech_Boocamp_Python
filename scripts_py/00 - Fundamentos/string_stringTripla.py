'''
STRING MULTIPLAS LINHAS

São definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem
ocupar várias linhas de código, e todos os espaços em branco são incuídos na string final.

'''

nome = "Paulo"

mensagem = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python.
        Esta mensagem tem diferentes recuos no texto.
"""
print(mensagem)

# Exemplo
#----------

print(
    """
    ========== MENU ==========

    1 - Depositar
    2 - Sacar
    3 - Sair

    ==========================

           Volte sempre!
    """
)