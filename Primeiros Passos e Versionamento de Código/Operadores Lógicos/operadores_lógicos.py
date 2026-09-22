# AND = para ser verdadeiro, todas as condições precisam ser verdadeiras
# OR = para ser verdadeiro, apenas uma das condições precisa ser verdadeira
# NOT = inverte o resultado de uma expressão booleana

saldo = 1000
saque = 200
limite = 1000
conta_especial = True

# Verifica se o saldo é maior ou igual ao saque e se o saque é menor ou igual ao limite
# Com o operador lógico "and", ambas as condições precisam ser verdadeiras para que o resultado seja True
print(saldo >= saque and saque <= limite)

# Verifica se o saldo é maior ou igual ao saque ou se o saque é menor ou igual ao limite
# Com o operador lógico "or", apenas uma das condições precisa ser verdadeira para que o resultado seja True
print(saldo >= saque or saque <= limite)

numeros_pares = [ ]

# Operador not inverte o resultado de uma expressão booleana
print(not 1000 > 1500)
print(not numeros_pares)
print(not "saque 1500;")
print(not "")

# Precedência de operadores lógicos: "and" tem precedência sobre "or"
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp)