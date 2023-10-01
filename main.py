tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla = tuple(range(11))
print(tupla)

tupla3 = ('Ciencia da Computação', 'Programação em Python')
escola, curso = tupla3
print(f'Na escola de {escola}')
print(f'estudando {curso}')

print(max(tupla1))
print(min(tupla1))
print(sum(tupla1))
print(len(tupla1))

print(tupla1 + tupla3)

tupla2 = tupla1 + tupla3
print(tupla2)

print(6 in tupla1)

for n in tupla1:
  print(n)

for indice, valor in enumerate(tupla1):
  print(indice, valor)

print(tupla1.count(1))

escola2 = tuple('Ciencia')
print(escola2)

##########

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses[5:9])

print(meses[5])

i = 0
while i < len(meses):
  print(meses[i])
  i = i + 1

##########

print(meses.index('Junho'))


