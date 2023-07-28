produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4
print(x)

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)   # Pela precedência primeiro (2**2), segundo (25*2)
z = (10 / 2) + 25 * ((2 - 2) ** 2)   # Pela precedência primeiro (10/2), depois (2-2)
print(x)
print(y)