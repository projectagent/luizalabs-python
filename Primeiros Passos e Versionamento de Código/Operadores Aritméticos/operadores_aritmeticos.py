# Adição
print (1+1)

# Subtração
print (10-2)

# Multiplicação
print (4 * 3)

# Divisão
print (10 / 2)

# Divisão inteira
print (10 // 3)

# Módulo - resto da divisão
print (10 % 3)

# Exponenciação
print (2 ** 3)

# Ordem de precedência
print (2 + 3 * 4) # Multiplicação tem precedência sobre adição
print ((2 + 3) * 4) # Parênteses têm precedência sobre multiplicação
print (10 ** 2 * 2) # Exponenciação tem precedência sobre multiplicação
print (10 ** (2 * 2)) # Parênteses têm precedência sobre exponenciação
print (10 / 2 * 4) # Divisão e multiplicação têm a mesma precedência, então são avaliadas da esquerda para a direita

# Boas práticas: deixar sempre evidente qual operação ocorre primeiro cmo parênteses, mesmo que a precedência 
# seja conhecida. Isso ajuda na legibilidade do código.

x = 40
y = 60

print (x + y * 2) # Multiplicação tem precedência sobre adição
print ((x + y) * 2) # Parênteses têm precedência sobre multiplicação
print (x + y * 2 / 4) # Multiplicação e divisão têm a mesma precedência, então são avaliadas da esquerda para a direita
print ((x + y) * 2 / 4) # Parênteses têm precedência sobre multiplicação e divisão
print (x + y * 2 / 4 - 5) # Multiplicação e divisão têm a mesma precedência, então são avaliadas da esquerda para a direita, depois subtração
print ((x + y * 2) / (4 - 5)) # Parênteses têm precedência sobre multiplicação, divisão e subtração