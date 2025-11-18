potencijalni_kodovi_fajl = open('potencijalni_kodovi.txt')
validni_kodovi_fajl = open('validni_kodovi.txt','w')

for linija in potencijalni_kodovi_fajl.readlines():
    linija_bez_novog_reda = linija.rstrip()
    #Kod je validan ako je brojA + brojT + brojG + brojC = duzina_koda
    broj_A = linija_bez_novog_reda.count('A')
    broj_T = linija_bez_novog_reda.count('T')
    broj_G = linija_bez_novog_reda.count('G')
    broj_C = linija_bez_novog_reda.count('C')
    duzina_koda = len(linija_bez_novog_reda)
    #Provera jednakosti zahteva dva jednako == da bi se razlikovala
    #od naredbe dodela, odnosno =
    if broj_A + broj_C + broj_G + broj_T == duzina_koda:
        validni_kodovi_fajl.write(linija)
    else:
        print(linija_bez_novog_reda)