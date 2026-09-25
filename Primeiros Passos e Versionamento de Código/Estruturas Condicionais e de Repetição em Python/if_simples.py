saldo = 2000.0
saque = float(input("Infomre o valor do saque: "))

# Estrutura condicional para ver se possui saldo ou não com dois if
if saldo >= saque:
    print("Realizando saque!")
if saldo <= saque:
    print("Saldo Insuficiente!")
