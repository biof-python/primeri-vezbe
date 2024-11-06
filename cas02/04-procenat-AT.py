my_dna = 'AATTAGCCTATTGTA'
duzina_koda = len(my_dna)
#AT ima 2 karaktera, count vraca broj ponavaljanja,
#Pa nam je za udeo potrebno da pomnozimo broj ponavljanja sa 2
udeo_AT = 2*my_dna.count('AT')/duzina_koda
print('AT cini ' + str(udeo_AT*100)+ '% procenata koda')