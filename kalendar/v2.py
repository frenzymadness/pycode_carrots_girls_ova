#!/usr/bin/env python3

# Rozšiřte řešení varianty 1 tak, aby dalším vstupem pro algoritmus byl
# den v týdnu (pondělí = 1, neděle = 7), na který připadá první den
# zadaného měsíce.

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

pocet_dni = dny[cislo_mesice]

print('   ' * start, end='')

for den in range(1, pocet_dni + 1):
    print(str(den).zfill(2), end=' ')

    if (start + den) % 7 == 0:
        print('')

print('')
