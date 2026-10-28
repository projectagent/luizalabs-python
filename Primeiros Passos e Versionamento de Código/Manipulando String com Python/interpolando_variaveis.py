# Três formas de interpolação: utilizando %, método format e f-strings

nome = "Arthur"
idade = 21
profissao = "Suporte Técnico"
linguagem = "Python"

# 1. Utilizando o operador % (estilo antigo / legatário)
# %s para string, %d para inteiros, %f para ponto flutuante
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# 2. Utilizando o método .format()
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# 2.1 Declarando sequencia dentro do .format
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

# 2.2 Declarando nome dentro do .format
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# 2.3 Desempacotando um dicionário com **
dados = {"nome": "Arthur", "idade": 21, "profissao": "Suporte Técnico", "linguagem": "Python"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))

# 3. Utilizando f-strings (método mais limpo e recomendado no Python moderno)
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# 3.1 Usando f-strings com expressãoes matemáticas
print(f"O dobro da minha idade é {idade * 2}.")

# 3.2 Formatando floats na f-string com f"{variavel:.2f}"
print(f"O dobro da minha idade é {idade * 2:.2f}.")

# 3.3 Formatar strings com f-strings e caracteres especiais
PI = 3.141592653589793
print(f"O valor de PI é {PI:10.2f}")