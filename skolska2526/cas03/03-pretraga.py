genetski_kod = 'ATGCATGCATGCATAG'

prvo_pojavljivanje_C = genetski_kod.find('C')
print('C se prvi put pojavljuje na poziciji:',prvo_pojavljivanje_C)

prvo_pojavljivanje_AT = genetski_kod.find('AT')
print('AT se prvi put pojavljuje na poziciji:',prvo_pojavljivanje_AT)

poslednje_pojavljivanje_c = genetski_kod.rfind('C')
print('C se poslednji put pojavljuje na poziciji:', poslednje_pojavljivanje_c)
