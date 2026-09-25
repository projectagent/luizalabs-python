# Solicita ao usuário que insira uma string (texto)
texto = input("Informe um texto: ")

# Define uma constante com as vogais em maiúsculo para referência na verificação
VOGAIS = "AEIOU"

# Laço de repetição 'for': itera sobre cada caractere (letra) da string 'texto'
for letra in texto:
    # Converte a letra atual para maiúscula e verifica se ela está contida na string VOGAIS
    if letra.upper() in VOGAIS:
        # Imprime a vogal encontrada. O parâmetro end="" evita a quebra de linha automática
        print(letra, end="")
 # Imprime uma quebra de linha ao final do laço para formatar a saída no console
else:
    print("Executado no final do laço")