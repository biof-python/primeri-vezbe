my_dna = 'AATTAGCCTATTGTA'
print(my_dna)
broj_ponavljanja_A = my_dna.count('A')
broj_ponavljanja_T = my_dna.count('T')
duzina_koda = len(my_dna)

procenatA= 100*broj_ponavljanja_A/duzina_koda
procenatB= 100*broj_ponavljanja_T/duzina_koda
print('A je: ' + str(procenatA)+ '% celog koda')
print('T je: ' + str(procenatB)+ '% celog koda')
#1. nacin
print('A i T cine: ' + str(procenatA+ procenatB)+ '% celog koda')
#2. nacin
udeo_A_i_T = (broj_ponavljanja_A + broj_ponavljanja_T)/duzina_koda
print('A i T cine: ' + str(udeo_A_i_T*100)+ '% celog koda')
