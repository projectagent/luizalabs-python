# Metodos da Classe List

# .sort() - Ordena a lista

numero = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

numero.sort()
print(numero) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# .sort(reverse=True) - Ordena a lista em ordem decrescente

numero = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

numero.sort(reverse=True)
print(numero) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# lambda x: len(x) - Ordena a lista em ordem crescente

numero = ["a", "b", "c", "d", "e"]

numero.sort(key=lambda x: len(x))
print(numero) # ["a", "b", "c", "d", "e"]

# Passando com reverse=true com lambda e x: len(x)
numero = ["a", "b", "c", "d", "e"]

numero.sort(key=lambda x: len(x), reverse=True)
print(numero) # ["e", "d", "c", "b", "a"]

# .reverse() - Inverte a ordem da lista

numero.reverse()
print(numero) # ["e", "d", "c", "b", "a"]

# .count() - Conta a quantidade de um elemento

numero = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]

print(numero.count(1)) # 1
print(numero.count(2)) # 2
print(numero.count(3)) # 3
print(numero.count(4)) # 4
print(numero.count(5)) # 0

l2 = numero.copy() # Cria uma cópia da lista
print(id(l2), id(numero)) # Mostra se tem o mesmo endereço de memoria

# .extend() - Adiciona elementos de outra lista

numero.extend([6, 7, 8, 9, 10])
print(numero) # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10]

# .index() - Retorna o indice de um elemento, não retorna todas as ocorrências, somente a primeira

print(numero.index(1)) # 0
print(numero.index(2)) # 1
print(numero.index(3)) # 3
print(numero.index(4)) # 6
print(numero.index(5)) # 10
print(numero.index(6)) # 11
print(numero.index(7)) # 12
print(numero.index(8)) # 13
print(numero.index(9)) # 14
print(numero.index(10)) # 15

# .pop() - Remove o ultimo elemento da lista também pode passar o indice do elemento que deseja remover

print(numero.pop()) # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]
print(numero.pop(0)) # [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]

# .remove() - Remove um elemento especifico, remove somente a primeira ocorrência

numero.remove(3)
print(numero) # [2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]

# .clear() - Limpa a lista

numero.clear()
print(numero) # []

# .reverse() - Inverte a ordem da lista

numero = [1, 2, 3, 4, 5]

numero.reverse()
print(numero) # [5, 4, 3, 2, 1]

# Len serve para ver o tamanho da lista

print(len(numero))

# Sorted serve para criar uma nova lista ordenada

print(sorted(numero)) # [1, 2, 3, 4, 5]

# Sorted reverse=True serve para criar uma nova lista ordenada em ordem decrescente

print(sorted(numero, reverse=True)) # [5, 4, 3, 2, 1]

# Sorted reverse=True com lambda e x: x.len() cria uma nova lista ordenada por tamanho em ordem decrescente

linguagens = ["Python", "Java", "C++", "C", "JavaScript", "Ruby", "Go", "Swift", "PHP", "Rust"]


print(sorted(linguagens, key=lambda x: len(x), reverse=True))
