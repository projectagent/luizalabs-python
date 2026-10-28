# Declaração da variável string com letras maiúsculas e minúsculas
curso = "PythON"

# Converte todos os caracteres para letras maiúsculas ('PYTHON')
print(curso.upper())

# Converte todos os caracteres para letras minúsculas ('python')
print(curso.lower())

# Converte a primeira letra de cada palavra para maiúscula e as demais para minúsculas ('Python')
print(curso.title())

# Remove os espaços em branco do início e do fim da string
curso = "   Python  "
print(curso.strip())

# Remove os espaços em branco do fim da string
print(curso.rstrip())

# Remove os espaços em branco do início da string
print(curso.lstrip())

# Centraliza a string em um tamanho total de 10 caracteres, preenchendo as bordas com o caractere informado ('##Python##')
curso = "Python"
print(curso.center(10, "#"))

# Concatena/junta cada caractere da string usando o separador informado ('P.y.t.h.o.n')
print(".".join(curso))

nome = "Arthur"
print(nome.upper())
print(nome.lower())
print(nome.title())

menu = "Python"
print("####"+ menu +"####")
print(menu.center(14))
print(menu.center(14, "#"))
