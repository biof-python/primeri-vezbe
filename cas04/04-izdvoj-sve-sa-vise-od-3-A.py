kodovi = open('kodovi.txt')
kodovi_sa_vise_od_3_A = open('kodovi_sa_vise_od_3_A.txt','w')

k=3

for kod in kodovi:
    if kod.count('A') > k:
        kodovi_sa_vise_od_3_A.write(kod)