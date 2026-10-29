# A diferença de tuplas e listas é que a tupla é imutável
# enquanto a lista é mutável
# Por isso existe a tupla para dados que não devem ser alterados
# As tuplas são definidas por parênteses
# Possui as mesmas propriedades das listas só que são imutáveis
# parentes são opcionais quando você define uma tupla
# Mas é boa prática usar parênteses para deixar claro que é uma tupla com uma virgula no final

frutas = ("Laranja", "Pera", "Uva",)

# transformando um iterável em tupla
letras = tuple("python")

numeros = tuple([1,2,3,4,5])

# Demostrando que tuplas com um elemento precisam de virgula
pais = ("Brasil",)

# Acessando o primeiro elemento
print(frutas[0])

# Acessando o ultimo elemento
print(letras[-1])

# Fatiamento
print(numeros[1:3])

# Tuplas são imutáveis
# frutas[0] = "Manga" # Isso geraria um erro

# O metodo .count() conta quantas vezes um elemento aparece na tupla
print(numeros.count(2))

# O metodo .index() mostra a posição de um elemento na tupla
print(letras.index("y"))

# O len() mostra o tamanho da tupla
print(len(frutas))

# Tuplas aninhadas desenhando matriz
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

print(matriz[1][1])