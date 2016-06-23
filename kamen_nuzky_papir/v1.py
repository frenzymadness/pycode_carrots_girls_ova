#!/usr/bin/env python3

# Naprogramujte jednoduchou variantu hry Kámen, nůžky, papír
# pro jednoho hráče a počítač. Hra musí splňovat následující požadavky
#
# Volba počítače je dána při startu hr
# Při startu budou vypsána základní pravidla hry
# Hráč bude vyzván k zadání své volby
# Hra porovná volbu hráče s volbu počítače dle známých pravidel
#   (kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen)
# Hra oznámí vítěze

pocitac = 'N'

print('Hra kamen, nuzky, papir')
print('Pravidla: kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen')

hrac = input('Zadejte svou volbu [K, N, P]: ')

if pocitac == hrac:
    print('Doslo k remize!')
elif (pocitac == 'K' and hrac == 'N') or (pocitac == 'N' and hrac == 'P') or (pocitac == 'P' and hrac == 'K'):
    print('Pocitac vyhral!')
else:
    print('Vyhral/a jste!')
