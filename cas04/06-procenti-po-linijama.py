kodovi = open('kodovi-06.txt')
procenti_u_kodu = open('procenti_u_kodu.txt','w')

for kod in kodovi:
    kod = kod.rstrip()
    procenat_A = 100*((kod.count('A'))/len(kod))
    procenat_G = 100*((kod.count('G'))/len(kod))
    procenat_C = 100*((kod.count('C'))/len(kod))
    procenat_T = 100*((kod.count('T'))/len(kod))
    #kod -> A: 25%, G:25%, C:25%, T: 25%
    izlazna_linija = kod + ' -> '
    izlazna_linija += 'A: ' +str(procenat_A)+'%, '
    izlazna_linija += 'G: ' +str(procenat_G)+'%, '
    izlazna_linija += 'C: ' +str(procenat_C)+'%, '
    izlazna_linija += 'T: ' +str(procenat_T)+'%'
    procenti_u_kodu.write(izlazna_linija+'\n')
    

