#!/usr/bin/env python3

# Upravte "inteligenci" počítače z varianty 3 tak, aby pravděpodobnost
# výběru některé ze 3 možností nebyla stejná, ale jedna z možností by
# měla mít pravděpodobnost 50% a zbylé dvě 25%. Při každém opakování hry
# je nutné pravděpodobnosti náhodně zamíchat.
#
# Například:
# - V prvním kole bude pravděpodobnost 50%, 25%, 25%
# - V druhém kole bude pravděpodobnost 25%, 50%, 25%

import random

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
    else:
        print('Vyhral/a jste!')

    pokracovat = input('Hrat dalsi kolo? [A/N]: ')

    if pokracovat == 'N':
        break
