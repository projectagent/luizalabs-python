# Cria um loop infinito utilizando 'while True'
# A repetição continuará indefinidamente até encontrar uma instrução de interrupção (break)
while True:
    # Solicita um número inteiro ao usuário a cada repetição
    numero = int(input("Informe um número: "))

    # Condição de parada: se o número digitado for igual a 10
    if numero == 10:
        # A instrução 'break' interrompe e encerra a execução do laço imediatamente
        break

    # Imprime o número caso a condição do 'break' não tenha sido atendida
    print(numero)