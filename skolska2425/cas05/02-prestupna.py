fajl_godine = open('godine.txt')
fajl_prestupne_godine = open('prestupne.txt','w')

#Godina je prestupna kada je deljiva sa 4
#I nije deljiva sa 100
#ili je deljiva 400

broj_pretupnih = 0
for linija in fajl_godine:
    godina = int(linija)
    if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 ==0:
        fajl_prestupne_godine.write(str(godina) + '\n')
        broj_pretupnih += 1

print('Broj prestupnih godina je: ' + str(broj_pretupnih))