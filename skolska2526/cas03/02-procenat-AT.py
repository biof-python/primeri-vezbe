genetski_kod = 'ATAGCTGACATGCATG'
broj_AT = genetski_kod.count('AT')
ukupna_duzina = len(genetski_kod)
procenat_AT = (2*broj_AT/ukupna_duzina)*100
print('AT cini',str(procenat_AT) + '% genetskog koda',genetski_kod)