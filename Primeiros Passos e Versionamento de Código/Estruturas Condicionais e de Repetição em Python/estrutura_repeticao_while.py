# Inicializa a variável com um valor diferente de 0 para garantir que o laço seja executado na primeira vez
opcao = -1

# O laço 'while' continua executando enquanto a condição (opcao diferente de 0) for verdadeira
while opcao != 0:
    # Exibe o menu interativo e captura a opção escolhida pelo usuário como inteiro
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    # Estruturas condicionais para executar a ação correspondente à opção escolhida
    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o extrato... ")

# Mensagem exibida fora do laço quando o usuário digita 0 e encerra a repetição
print("Finalizando")

# Exemplo de uso da instrução 'break' dentro de um laço 'for':
# Interrompe completamente o laço assim que a condição for satisfeita
for numero in range(100):
    if numero == 12:
        break  # Encerra o loop ao atingir o número 12
    print(numero, end=" ")

print("\n")

# Exemplo de uso da instrução 'continue' dentro de um laço 'for':
# Pula o restante da iteração atual e avança direto para a próxima volta do laço
for numero in range(100):
    # 'numero % 2' retorna 1 para números ímpares (verdadeiro em Python)
    if numero % 2:
        continue  # Pula os números ímpares, imprimindo apenas os pares
    print(numero, end=" ")