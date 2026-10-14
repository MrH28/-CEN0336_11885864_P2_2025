#!/usr/bin/env python3

# Solicita ao usuário uma sequência de DNA e padroniza as letras para maiúsculas.
sequencia = input("Digite uma sequência de DNA: ").strip().upper()


# Verifica se a sequência contém apenas nucleotídeos válidos.
nucleotideos_validos = "ATCG"
if not sequencia or any(nucleotideo not in nucleotideos_validos for nucleotideo in sequencia):
    print("Erro: informe uma sequência contendo apenas as letras A, T, C e G.")
    raise SystemExit(1)


# Inicializa as contagens de cada nucleotídeo.
contagem_a = 0
contagem_t = 0
contagem_c = 0
contagem_g = 0


# Percorre a sequência e incrementa a contagem do nucleotídeo encontrado.
for nucleotideo in sequencia:
    if nucleotideo == "A":
        contagem_a += 1
    elif nucleotideo == "T":
        contagem_t += 1
    elif nucleotideo == "C":
        contagem_c += 1
    else:
        contagem_g += 1


# Exibe a quantidade de vezes que cada nucleotídeo aparece.
print(f"A: {contagem_a}")
print(f"T: {contagem_t}")
print(f"C: {contagem_c}")
print(f"G: {contagem_g}")
