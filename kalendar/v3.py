#!/usr/bin/env python3

# Pomocí řešení z varianty 2 vypište kalendář na celý rok. Vstupem bude
# opět jméno měsíce a den v týdnu, na který připadá první den zadaného
# měsíce.

import sys

zadany_mesic = sys.argv[1]
start = int(sys.argv[2]) - 1

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

dalsi_start = 0

# Iterujeme pro dvanact mesicu od zadaneho mesice
for mesic in range(cislo_mesice, cislo_mesice + 12):

    # Pokud jsme dosli na konec seznamu, zacneme indexy pocitat od zacatku
    if mesic > 11:
        mesic = mesic - 12

    pocet_dni = dny[mesic]

    print(mesice[mesic] + '\n\n')

    # Odsazeni prvniho tydne o pocet dni v promenne start
    print('   ' * start, end='')

    # Cyklus pro jednotlive dny
    for den in range(1, pocet_dni + 1):
        print(str(den).zfill(2), end=' ')

        den_v_tydnu = (start + den) % 7

        if den_v_tydnu == 0:
            print('')

        # Informace o tom, kde ma zacit dalsi mesic (prubezne aktualizovano)
        dalsi_start = den_v_tydnu

    # Ulozime, kde ma zacit dalsi mesic v novem cyklu
    start = dalsi_start

    print('\n\n')
