kodovi = open('kodovi.txt')
prebrojani_A_fajl = open('prebrojani_A.txt','w')

#1. korak: ispisacemo linije na standardni izlaz
#kodovi.readlines nam vraca listu: ATTTAACCTGTTTACC\n, TTGCTTATTGC\n, AGCCTTGAAATTTTGC\n, TTAAA\n
#I zato moramo da budemo obazrivi sa \n. Na narednim casovima cemo raditi detaljnije

# for linija in kodovi.readlines():
#     print(linija.rstrip())
#     #print('Kraj petlje') -> Na ovaj nacin bi nakon svake linije bilo ispisano: Kraj petlje
# print('Kraj petlje')

#2. korak: ispisujemo linije u fajl
# for linija in kodovi.readlines():
#     prebrojani_A_fajl.write(linija.rstrip() + '\n')
#     # mogli smo reci za 2. korak i samo prebrojani_A_fajl.write(linija)

#3. korak: Prebrojimo A u liniji:
for linija in kodovi.readlines():
    linija_bez_novog_reda = linija.rstrip()
    broj_A = linija_bez_novog_reda.count('A')
    prebrojani_A_fajl.write(linija_bez_novog_reda + ': ' +str(broj_A)+'A' +'\n')
    #Moguca greska:
    #prebrojani_A_fajl.write(linija + ': ' +str(broj_A)+'A' +'\n')
