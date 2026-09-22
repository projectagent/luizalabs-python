curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# IS verifica se as variaves estão na mesma região de memória
print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)