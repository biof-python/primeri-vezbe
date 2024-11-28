fajl_kodovi = open('kodovi.txt')
fajl_kodovi_na_A = open('kodovi_na_A.txt','w')

broj_kodova = 0
broj_kodova_na_A = 0

for linija in fajl_kodovi:
    kod = linija
    broj_kodova += 1
    if kod[0] == 'A':
        fajl_kodovi_na_A.write(kod)
        broj_kodova_na_A += 1

print('Ukupno ima: ' + str(broj_kodova) +' kodova')
print('Ukupno ima: ' + str(broj_kodova_na_A) +' kodova na A')