# Importa o módulo sys para utilizar funções do sistema, como sys.exit()
import sys

# Solicita ao usuário a escolha de uma opção do menu e converte para número inteiro
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

# Estrutura condicional para direcionar o fluxo de acordo com a opção escolhida
if opcao == 1:
    # Opção de saque: solicita a quantia a ser sacada
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    # Opção de extrato: exibe mensagem informativa
    print("Exibindo o extrato ...")
else:
    # Caso seja digitada qualquer outra opção, finaliza a execução exibindo mensagem de erro
    sys.exit("Opção inválida")

