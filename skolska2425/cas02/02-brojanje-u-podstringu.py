my_dna = 'AATTAGCCTATTGTA'
# manji_primer = 'ATTA'
# print(str(manji_primer.count('T',1,2)))
#TAGCCTATT
print('Od drugog do cetvrtog kodona imamo ' + str(my_dna.count('T',3,12)) +' ponavaljanja T')
#2. nacin
trazeni_kodoni = my_dna[3:12]
print(trazeni_kodoni)
print('Od drugog do cetvrtog kodona imamo ' + str(trazeni_kodoni.count('T')) +' ponavaljanja T')
#3. nacin
trazeni_kodoni1 = my_dna[3:-3]
print(trazeni_kodoni1)
print('Od drugog do cetvrtog kodona imamo ' + str(trazeni_kodoni1.count('T')) +' ponavaljanja T')

