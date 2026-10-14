#!/usr/bin/env python3

# Importa o módulo sys para acessar os argumentos da linha de comando.
import sys


# Confere se foram fornecidos exatamente uma sequência e seis coordenadas.
if len(sys.argv) != 8:
    print("Erro: informe uma sequência de DNA e seis números inteiros.")
    sys.exit(1)


# Armazena a sequência e verifica se ela contém somente nucleotídeos válidos.
sequencia = sys.argv[1].upper()
if not sequencia or any(nucleotideo not in "ATCG" for nucleotideo in sequencia):
    print("Erro: a sequência deve conter apenas os nucleotídeos A, T, C e G.")
    sys.exit(1)


# Converte as seis coordenadas para inteiros e informa entradas inválidas.
coordenadas_texto = sys.argv[2:]
if not all(coordenada.isdigit() for coordenada in coordenadas_texto):
    print("Erro: as seis coordenadas devem ser números inteiros positivos.")
    sys.exit(1)

coordenadas = [int(coordenada) for coordenada in coordenadas_texto]
n1, n2, n3, n4, n5, n6 = coordenadas


# Verifica se as coordenadas estão dentro da sequência e em ordem crescente.
if any(coordenada > len(sequencia) for coordenada in coordenadas):
    print("Erro: nenhuma coordenada pode ser maior que o tamanho da sequência.")
    sys.exit(1)

if any(coordenada <= 0 for coordenada in coordenadas) or coordenadas != sorted(coordenadas):
    print("Erro: as coordenadas devem ser positivas e estar em ordem crescente.")
    sys.exit(1)


# Extrai as duas regiões entre CDS consecutivas, usando coordenadas inclusivas.
intron_1 = sequencia[n2:n3 - 1]
intron_2 = sequencia[n4:n5 - 1]


# Confere se cada intron começa com GT e termina com AG.
introns_validos = (
    intron_1.startswith("GT")
    and intron_1.endswith("AG")
    and intron_2.startswith("GT")
    and intron_2.endswith("AG")
)

if not introns_validos:
    print("Erro: as regiões entre as CDS devem começar com GT e terminar com AG.")
    sys.exit(1)


# Extrai as três CDS e concatena suas sequências.
cds_1 = sequencia[n1 - 1:n2]
cds_2 = sequencia[n3 - 1:n4]
cds_3 = sequencia[n5 - 1:n6]
cdna = cds_1 + cds_2 + cds_3


# Exibe a sequência resultante da junção das três CDS.
print(cdna)
