#!/usr/bin/env python3

# Do hry z varianty 1 přidejte validaci uživatelského vstupu.
# Hra dá uživateli na výběr následující položky A. Kámen B. Nůžky C. Papír D. Konec hry
# Hra se navíc musí po oznámení vítěze zeptat, jestli má zahájit nové kolo.

pocitac = 'N'

print('Hra kamen, nuzky, papir')
print('Pravidla: kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen')

while True:

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
