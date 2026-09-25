# Definição dos tipos de conta através de variáveis booleanas
conta_normal = True
conta_universitaria = False

# Valores de saldo, valor solicitado para saque e limite de cheque especial
saldo = 2000
saque = 2500
cheque_especial = 450

# Verificação principal: Tipo da conta
if conta_normal:
    # Estruturas condicionais aninhadas para conta normal
    if saldo >= saque:
        print("Saque Realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo Insuficiente!")
elif conta_universitaria:
    # Estruturas condicionais aninhadas para conta universitária (sem cheque especial)
    if saldo >= saque:
        print("Saque Realizado!")
    else:
        print("Saldo Insuficiente!")
else:
    # Caso nenhuma das opções de conta seja verdadeira
    print("Tipo de conta inválida!")

