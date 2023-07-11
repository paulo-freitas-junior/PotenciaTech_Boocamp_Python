# INT PARA FLOAT
#---------------
preco = 10
print(preco)
print(type(preco))

preco = float(preco)   # conversão
print(preco)
print(type(preco))

preco = 10 / 2
print(preco)
print(type(preco))

# FLOAT PARA INT
#--------------
preco = 10.30
print(type(preco))
print(preco)

print (preco / 2)

print (preco // 2)   # Uso das '//' pega resultado apenas inteiro da divisão


# NUMERICO PARA INT
#------------------
preco = 10.50
idade = 28

print(str(preco))
print(type(preco))  # preco se mantem numerico como original mas impresso como Sting
print(preco)

print(str(idade))

texto = f"idade {idade} preco {preco}"    # CONCATENA textos do usuário com variaveis
print(texto)

# STR PARA NUMÉRICO
#------------------
preco = "10.50"
idadeo = "28"

print(float(preco))
print(type(preco))   # preco se mantem como Sting mas impressço como Float
print(preco)

print(int(idade))   # idade se mantem como Sting mas impressço como Float