#!/usr/bin/env python3

# Hra by měla sbírat statistiky hráčů pro každé kolo.
# Na závěr vypište následující údaje
# - Počet výher hráče
# - Počet výher počítače
# - Jméno celkového vítěze
# - Procentuální úspěšnost hráče i počítače
# - Nejdelší výherní posloupnost pro hráče i počítač

import random

vyhry_hrace = 0
vyhry_pocitace = 0
pocet_kol = 0

print('Hra kamen, nuzky, papir')
print('Pravidla: kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen')

while True:

    moznosti = ['K', 'N', 'P']

    # Vybereme jednu moznost nahodne
    moznost = random.choice(['K', 'N', 'P'])

    # A pridame ji zpet do seznamu moznosti
    # nyni je tam jedna dvakrat a proto ma 50% pravdepodobnost - 2/4
    moznosti.append(moznost)

    pocitac = random.choice(moznosti)

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
        vyhry_pocitace += 1
    else:
        print('Vyhral/a jste!')
        vyhry_hrace += 1

    pocet_kol += 1

    pokracovat = input('Hrat dalsi kolo? [A/N]: ')

    if pokracovat == 'N':
        break

if pocet_kol > 0:
    print('Pocet vyher pocitace: {} tj. {} %'.format(vyhry_pocitace, vyhry_pocitace / pocet_kol * 100))
    print('Pocet vyher hrace: {} tj. {} %'.format(vyhry_hrace, vyhry_hrace / pocet_kol * 100))

    if vyhry_pocitace == vyhry_hrace:
        print('Remiza!')
    elif vyhry_hrace > vyhry_pocitace:
        print('Hrac je celkovym vitezem!')
    else:
        print('Pocitac je celkovym vitezem!')
