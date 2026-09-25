conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo Insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado!")
    else:
        print("Saldo Insuficiente!")
else:
    print("Tipo de conta inválida!")

