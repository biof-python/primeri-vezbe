genetski_kod = 'ATGCGCTAGCGGCCCGTAAT'
print(genetski_kod)
duzina_koda = len(genetski_kod)
broj_A = genetski_kod.count('A')
print('U nasem kodu imamo ' + str(broj_A) + ' ponavljanja A')
procenat_A = (broj_A/duzina_koda)*100
print('To je ukupno: ' + str(procenat_A) +' %')
