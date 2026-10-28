# Fatiando String em Python

# Declaração da string
nome = "Arthur Carlos Oliveira Rossini"

# Retorna apenas o caractere no índice 0 (primeira letra): 'A'
print(nome[0])

# Retorna do início da string até o índice 6 (índice 6 não é incluído): 'Arthur'
print(nome[:6])

# Retorna do índice 7 até o fim da string: 'Carlos Oliveira Rossini'
print(nome[7:])

# Retorna do índice 7 até o índice 13 (índices 7 a 12): 'Carlos'
print(nome[7:13])

# Fatiamento com índice negativo: pega do 7º caractere de trás para frente até o fim: 'Rossini'
print(nome[-7:])

# Equivalente a nome[:6], definindo o início explicitamente no índice 0: 'Arthur'
print(nome[0:6])

# Retorna pulando de 2 em 2 caracteres: 
print(nome[0:13:2])

# Retorna invertendo a ordem da string
print(nome[::-1])

# String com Aspas Triplas e Formatação f-string
# Mante toda a identação, montar menu ou mensagem grande
print(f"""

   Olá meu nome é {nome}
   Eu tenho {20} anos.

""")

print("""
    =========== MENU ==============
    1 - Cadastrar
    2 - Alterar
    3 - Excluir
    4 - Sair
    ===============================
    
            Obrigado por usar o sistema!


""")