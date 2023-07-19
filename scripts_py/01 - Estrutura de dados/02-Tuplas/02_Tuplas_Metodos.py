'''
MÉTODOS EM DUPLAS
'''

# >> [].count()
cores = ('vermelhor','azul','verde','azul',)
print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))


# >> [].index()
linguagens = ('python','js','c','java','csharp',)
print(linguagens.index('python'))
print(linguagens.index('c'))


# >> [].len()
linguagens = ('python','js','c','java','csharp',)
print(len(linguagens))


carros = ('gol')
print(isinstance(carros,tuple))
