# Em Python tudo é objeto, até mesmo listas
# Uma lista é uma coleção ordenada e mutável de elementos de qualquer tipo mesmo misturados
# Exemplo: lista de números, lista de strings, lista de listas,etc.

# Criando listas
frutas = ["Laranja", "Maçã", "Uva", "Manga"]
print(frutas)

# Criando listas com list()
letras = list("banana")
print(letras)

# Criando listas com range()
numeros = list(range(10))
print(numeros)

# Criando listas com diferentes tipos de dados
carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto e slicing
print(carro[0]) # Ferrari
print(carro[1]) # F8
print(carro[2]) # 420000
print(carro[3]) # 2020
print(carro[4]) # 2900
print(carro[5]) # São Paulo
print(carro[-1]) # True

# Fatiamento
print(carro[0:3]) # ['Ferrari', 'F8', 420000]

# Acessando inversamente
print(carro[-1]) # True
print(carro[-2]) # São Paulo
print(carro[-3]) # 2900
print(carro[-4]) # 2020
print(carro[-5]) # 420000
print(carro[-6]) # F8
print(carro[-7]) # Ferrari

# Listas Aninhadas (List of Lists)
# Criando listas aninhadas
matriz = [["A", "B", "C"], 
          [ 1,   2,   3], 
          [4.5, 6.7, 8.9]]
print(matriz)

# Acessando elementos em listas aninhadas 
print(matriz[0]) # ["A", "B", "C"]
print(matriz[1]) # [1, 2, 3]
print(matriz[2]) # [4.5, 6.7, 8.9]

# Chamando elementos individuais
print(matriz[0][0]) # A
print(matriz[0][1]) # B
print(matriz[-1][-1]) # C

# Chamando elementos individuais inversos
print(matriz[1][0]) # 1
print(matriz[1][-1]) # 3
print(matriz[1][2]) # 3

print(matriz[2][0]) # 4.5
print(matriz[2][1]) # 6.7
print(matriz[2][-1]) # 8.9

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[1:6]) # ["y", "t", "h", "o", "n"]
print(lista[:]) # ["p", "y", "t", "h", "o", "n"]
print(lista[:3]) # ["p", "y", "t"]
print(lista[3:]) # ["h", "o", "n"]
print(lista[:-3]) # ["p", "y", "t"]

# Listas são mutáveis, podemos alterar, adicionar ou remover elementos

lista_a = [1, 2, 3]
lista_a[0] = 4 # Alterando o primeiro elemento
print(lista_a) # [4, 2, 3]

lista_b = [1, 2, 3]
lista_b.append(4) # Adicionando um elemento ao final
print(lista_b) # [1, 2, 3, 4]

lista_c = [1, 2, 3]
lista_c.remove(1) # Removendo um elemento pelo valor
print(lista_c) # [2, 3]

lista_d = [1, 2, 3]
lista_d.pop() # Removendo o último elemento
print(lista_d) # [1, 2]

lista_e = [1, 2, 3]
lista_e.pop(0) # Removendo um elemento pelo índice
print(lista_e) # [2, 3]

# Filtro de Listas
numero = [1, 30, 55, 7, 99, 120]

# Criando uma nova lista com números pares
pares = []
for n in numero:
    if n % 2 == 0:
        pares.append(n)
print(pares) # [30, 120]

# List Comprehension
numeros = [1, 30, 55, 7, 99, 120]
pares = [n for n in numeros if n % 2 == 0]
print(pares) # [30, 120]

# List Comprehension com if else
numeros = [1, 30, 55, 7, 99, 120]
pares = ["par" if n % 2 == 0 else "ímpar" for n in numeros]
print(pares) # ['ímpar', 'par', 'ímpar', 'ímpar', 'ímpar', 'par']