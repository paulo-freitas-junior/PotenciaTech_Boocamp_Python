'''
FATIAMENTO DE STRING -- SLICE

Técnica utilizada para retornar substrings (partes da string original), informando
inicio(start), fim(stop), e passo(step)

[start: stop[,step]]

'''

nome = "Paulo Roberto Lopes de Freitas Jr"

print(nome[0])
print(nome[:9])        # caracter 0 ao 8 (último não é incluído)
print(nome[10:])       # inicia à partir do 10 caracter
print(nome[10:16])     # Início 10 término 15 caracter (último não é incluído)
print(nome[10:16:2])   # Início 10 término 15 caracter PULANDO 2 em 2 caracters (último não é incluído)
print(nome[:])         # Retorna valor completo
print(nome[::-1])      # Retorna a string ESPELHADA inversa
