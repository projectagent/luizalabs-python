# Valores iniciais de saldo e saque
saldo = 500
saque = 400

# Operador ternário (expressão condicional em uma única linha):
# sintaxe: <retorno_se_verdadeiro> if <condicao> else <retorno_se_falso>
status = "Sucesso" if saldo >= saque else "Falha"

# Exibe o resultado utilizando interpolação de strings (f-string)
print(f"{status} ao realizar o saque!")