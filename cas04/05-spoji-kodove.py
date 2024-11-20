kodovi_sa_brojem_ponavljanja = open('kodovi_sa_brojem_ponavljanja.txt')

spojen_kod = ''
for linija in kodovi_sa_brojem_ponavljanja:
    kod_i_broj = linija.split(',') #['AT','2']
    kod = kod_i_broj[0]
    broj = int(kod_i_broj[1])
    spojen_kod_u_liniji = ''
    #Posto nam i nije bitno mogli smo da napisemo i
    #for _ in range(broj):
    for i in range(broj): 
        spojen_kod_u_liniji += kod.rstrip()
    spojen_kod += spojen_kod_u_liniji

print(spojen_kod)