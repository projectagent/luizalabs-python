# Definição de constantes para as idades de referência
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

# Entrada de dados convertida para inteiro
idade = int(input("Informe sua idade: "))

# Exemplo 1: Uso de estruturas condicionais simples (if separado)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade <= MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

# Exemplo 2: Uso de estrutura condicional composta (if-else)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

# Exemplo 3: Uso de estrutura condicional aninhada/múltipla (if-elif-else)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas mas não pode fazer as práticas")
else:
    print("Ainda não pode tirar a CNH")
