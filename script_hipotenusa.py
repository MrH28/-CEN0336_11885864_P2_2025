#!/usr/bin/env python3

# Importa o módulo sys para acessar os argumentos da linha de comando.
import sys


# Confere se os argumentos fornecidos são dois inteiros positivos menores que 500.
if len(sys.argv) != 3:
    print("Erro: informe exatamente dois inteiros positivos menores que 500.")
    sys.exit(1)

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Erro: os dois argumentos devem ser inteiros positivos.")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

if not (0 < a < 500 and 0 < b < 500):
    print("Erro: os dois inteiros devem ser positivos e menores que 500.")
    sys.exit(1)


# Calcula o quadrado da hipotenusa usando o teorema de Pitágoras.
quadrado_hipotenusa = a**2 + b**2


# Exibe o resultado no formato solicitado.
print(
    f"O quadrado da hipotenusa para o triangulo retângulo "
    f"com lados a={a} e b={b}, é {quadrado_hipotenusa}"
)
