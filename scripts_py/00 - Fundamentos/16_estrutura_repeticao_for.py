'''
ESTRUTURAS DE REPETIÇÃO

Utilizadas para repetir um trecho de código determinado número de veses. Esse número pode
ser conhecido previamente, ou determinado através de uma expressão lógica.

>> FOR
É usado para percorrer um objeto interável. Faz sentido usar quando sabemos o número exato
de vezes que nosso bloco de c´pdigo deve ser executado, ou quando queremos percorrer um
objeto iterável.

'''
# EXEMPLO 1 - Interável
#=========================================
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"    # Constante

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()     # adiciona uma quebra de linha


# EXEMPLO 2 - Interável
#=========================================
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"    # Constante

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()     # adiciona uma quebra de linha
    print("Texto está vazio!")


# ----------------------------------------------------------------------------
'''
>> FUNÇÃO RANGE

Função  built-in do Python, ela é usada para produzir uma sequência de números
inteiros a partir de um início(inclusivo) para um fim(exclusivo). Se usarmos
range(i,j) será produzido:

i, i+1, i+2, i+3, ..., j-1

Ela recebe 3 argumentos: stop(obrigatório), start(opcional), step(opcional)

'''
# range(start, stop, step)

# Exemplo 3
#----------
for numero in range(0,11):      # 0 à 10
    print(numero, end=" ")      # end faz o resultado ficar na mesma linha


# Exemplo 4 - exibindo a tabuada do 5
#----------
for numero in range(0, 51, 5):  # de 0 a 50
    print(numero, end=" ")      # end faz o resultado ficar na mesma linha
