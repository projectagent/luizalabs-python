# A função built-in range() produz uma sequência numérica iterável.
# Diferente de iterar diretamente sobre um iterável existente (como uma string ou lista),
# o range() gera os números sob demanda para serem consumidos pelo laço 'for'.

# Exemplo 1: Utilizando range com (start, stop)
# O laço irá iterar de 0 até 10 (o limite final, 11, é exclusivo)
for numero in range(0, 11):
    print(numero, end=" ")

print() # Quebra de linha para separar as impressões no console

# Exemplo 2: Utilizando range com (start, stop, step)
# O laço irá iterar de 0 até 50, com incrementos (passos) de 5 em 5
for numero in range(0, 51, 5):
    print(numero, end=" ")