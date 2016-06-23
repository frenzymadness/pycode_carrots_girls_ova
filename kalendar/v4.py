#!/usr/bin/env python3

# Do řešení varianty 3 přidejte podporu pro přestupné roky.
# Pravidlo pro přestupný rok (dle Juliánského kalendáře) je následující
# Je-li rok dělitelný 400, je vždy přestupný
# Je-li rok dělitelný 100, není přestupný
# Je-li rok dělitelný 4, je přestupný, neplatí-li pravidlo č. 2
# Vstupem u této varianty bude pouze rok. Den v týdnu pro první leden
# daného roku bude nutné spočítat. Při tomto výpočtu využijte znalosti
# toho, že 1. ledna 1900 bylo pondělí.

import sys

zadany_rok = int(sys.argv[1])

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

dalsi_start = 0


# Funkce zjistujici, zda je zadany rok prestupny rok ci ne
def je_prestupny(rok):
    if rok % 400 == 0:
        return True
    elif rok % 4 == 0 and rok % 100 != 0:
        return True
    else:
        return False

# Vypocet poctu dni (prestupnych let) mezi rokem 1900 a zadanym rokem
pocet_dni = 0
for rok in range(1900, zadany_rok):
    if je_prestupny(rok):
        pocet_dni += 366
    else:
        pocet_dni += 365

# Pocet dni mezi prvn9m lednem roku 1900 a zadanym rokem delen poctem dni v tydnu
start = pocet_dni % 7

# Iterujeme pro dvanact mesicu od zadaneho mesice
for mesic in range(0, 12):

    # Pokud jsme dosli na konec seznamu, zacneme indexy pocitat od zacatku
    if mesic > 11:
        mesic = mesic - 12

    pocet_dni = dny[mesic]

    if mesic == 1 and je_prestupny(zadany_rok):
        pocet_dni = 29

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
