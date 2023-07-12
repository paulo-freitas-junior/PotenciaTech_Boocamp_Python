'''
A estrutura condicional permite o desvio de fluxo de controle, quando
determinadas expressões lógicas são atendidas.

IF
Cria uma estrutura condicional simples, composta por um único desvio, podemos utilizar
a palavra reservada IF.
O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações 
presentes no bloco de código do IF serão executadas.

'''
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

'''
IF/ELSE
Cria uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas
if e else. Como sabemos se a expressão lógica testada no IF for verdadeira, então o bloco
de código do IF será executado. Caso contrário o bloco de código do else será executado.

'''
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

''''
IF/ELIF/ELSE
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra 
reservada ELIF. O elif é composto por uma nova expressão lógica, que será testada e caso
retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo
de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois 
elas aumentam a complexidade do código.

'''
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ....
elif opcao == 2:
    print("Exibindo o extrato")
else:
    sys.exit("Opção inválida")


#-------------------------------------------------------------------------

MAIOR_IDADE = 18   # Lembrando que é uma constante, por isso em maiúsculas
IDADE_ESPECIAL = 17

idade = int(input("Informe a idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")

else:
    print("Ainda não pode tirar CNH")