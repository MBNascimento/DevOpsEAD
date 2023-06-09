#Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3])
print(lanche[-2:])
print(lanche[-3:])
print(lanche)
print(lanche[1])

for comida in lanche:# PRIMEIRO FOR
    print(f'Eu vou comer {comida}')
print('Comi pra caramba !') # primeiro metodo for é com variável composta , mesmo resultado do for in range formatado.

print(len(lanche))

for cont in range(0, len(lanche)):# mostra a quantidade em numeros de lanche
    print(cont)

for cont in range(0, len(lanche)):# mostra os componentes do lanche
    print(lanche[cont])

for cont in range(0, len(lanche)):# SEGUNDO FOR
    print(f'EU VOU COMER {lanche[cont]}')# for in range formatado mostra o mesmo resultado que o for in lanche composto(anterior).

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#primeiro for pra mostrar posição.

for pos, comida in enumerate(lanche):
    print(f'Vamos comer {comida} na posição {pos}')#segundo for pra mostrar posiçao

print('COMI PRA CARAMBA!')

print(sorted(lanche))# metodo sorted mostra na ordem crescente ( alfabética)
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
c1 = b + a
# quando concatenamos tuplas a soma não segue a ordem da matemática tradicional , a ordem aqui tem interferência

print(c)
print(len(c))# método len() mostra quantos elementos tem na tupla.
print(c.count(2))# metodo, .cout() mortra quantas vezes o número aparece na tupla.
print(c.count(9))# se colocado um valor que não existe sera mostrado valor zero .
print(c1)
print(c1.index(8))# propriedade index mostra em que posição esta o numero oito
print(c1.index(2))# mostra somente a primeira ocorrencia do número dois
print(c1.index(5, 1))# (deslocamento mostra o número na posição apartir da referencia.

# as tuplas no PYTHON aceita dados se diferentes tipos primitivos

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)















