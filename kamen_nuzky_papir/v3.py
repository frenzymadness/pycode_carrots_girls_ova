#!/usr/bin/env python3

# Upravte implementaci varianty 2 tak, aby počítač při každém novém
# startu hry vybral svou odpověď náhodně. Pro generování náhodných čísel
# použijte modul random. Návod na použití tohoto modulu naleznete on-line
# na https://docs.python.org/3/library/random.html nebo off-line
# v interpretu pythonu pomocí sekvence příkazů
#
# >>> import random
# >>> help(random)

import random

print('Hra kamen, nuzky, papir')
print('Pravidla: kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen')

while True:

    pocitac = random.choice(['K', 'N', 'P'])

    hrac = input('Zadejte svou volbu [K, N, P] nebo "Q" pro konec hry: ')

    if hrac == 'Q':
        break

    if hrac != 'K' and hrac != 'N' and hrac != 'P':
        print('Nespravne zadani!')
        continue

    if pocitac == hrac:
        print('Doslo k remize!')
    elif (pocitac == 'K' and hrac == 'N') or (pocitac == 'N' and hrac == 'P') or (pocitac == 'P' and hrac == 'K'):
        print('Pocitac vyhral!')
    else:
        print('Vyhral/a jste!')

    pokracovat = input('Hrat dalsi kolo? [A/N]: ')

    if pokracovat == 'N':
        break
