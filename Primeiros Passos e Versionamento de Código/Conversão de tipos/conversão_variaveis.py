# =====================================================================
# CONVERSÃO DE TIPOS (CASTING)
# =====================================================================
# type() retorna o tipo real da variável em tempo de execução.

# ---------------------------------------------------------------------
# int -> float
# ---------------------------------------------------------------------
preco = 10 
print(preco)            # 10
print(type(preco))      # <class 'int'>
preco = float(preco)    # converte int para float
print(preco)            # 10.0
print(type(preco))      # <class 'float'>

# Divisão sempre resulta em float
preco = 10/2
print(preco)            # 5.0
print(type(preco))      # <class 'float'>

# ---------------------------------------------------------------------
# float -> int
# ---------------------------------------------------------------------
preco = 10.30
print(preco)            # 10.3
print(type(preco))      # <class 'float'>
preco = int(preco)      # converte float para int (trunca as casas decimais)
print(preco)            # 10
print(type(preco))      # <class 'int'>

# ---------------------------------------------------------------------
# Divisão comum vs divisão inteira
# ---------------------------------------------------------------------
preco = 10
print(preco)            # 10
print(type(preco))      # <class 'int'>
print(preco / 2)        # 5.0 -> float (divisão comum)
print(type(preco / 2))  # <class 'float'>
print(preco // 2)       # 5   -> int (divisão inteira)
print(type(preco // 2)) # <class 'int'>

# ---------------------------------------------------------------------
# Números -> str
# ---------------------------------------------------------------------
preco = 10.50
idade = 28
print(str(preco))       # converte float para str
print(type(str(preco))) # <class 'str'>
print(str(idade))       # converte int para str
print(type(str(idade))) # <class 'str'>

# f-string: formata os valores como texto automaticamente
texto = f"idade: {idade}\npreço: {preco}"
print(texto)            # idade: 28 preço: 10.5
print(type(texto))      # <class 'str'>

# ---------------------------------------------------------------------
# str -> int / float
# ---------------------------------------------------------------------
preco = "10.50"
idade = "28"
print(float(preco))     # converte str para float -> 10.5
print(type(float(preco)))   # <class 'float'>
print(int(idade))       # converte str para int -> 28
print(type(int(idade)))     # <class 'int'>

# Atenção: a conversão só funciona se o texto for numérico.
# Textos como "python" geram erro (ValueError).
preco = "python" 
print(float(preco))     # erro: não é possível converter str para float 