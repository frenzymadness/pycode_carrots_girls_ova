#!/usr/bin/env python3

# Cílem této úlohy je vypsat kalendář pro konkrétní měsíc. Vstupem bude
# jméno měsíce (česky nebo anglicky). Přestupné roky neberte v úvahu
# (tj. únor bude mít vždy 28 dnů).

import sys

zadany_mesic = sys.argv[1]

mesice = ['leden',
          'unor',
          'brezen',
          'duben',
          'kveten',
          'cerven',
          'cervenec',
          'srpen',
          'zari',
          'rijen',
          'listopad',
          'prosinec']

dny = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cislo_mesice = mesice.index(zadany_mesic)

pocet_dni = dny[cislo_mesice]

for den in range(1, pocet_dni + 1):
    print(str(den).zfill(2), end=' ')

    if den % 7 == 0:
        print('')

print('')
