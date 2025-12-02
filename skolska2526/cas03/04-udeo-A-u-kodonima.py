genetski_kod = 'ATGACATAGACTTAGCT'
#1. nacin:
prva_dva_kodona = genetski_kod[:6]
print(prva_dva_kodona)
poslednja_dva_kodona = genetski_kod[-6:]
print(poslednja_dva_kodona)
procenat_A_prva_dva = prva_dva_kodona.count('A')/len(prva_dva_kodona)*100
procenat_A_poslednja_dva = poslednja_dva_kodona.count('A')/len(poslednja_dva_kodona)*100
print('A cini',procenat_A_prva_dva,'procenata prva 2 kodona')
print('A cini',procenat_A_poslednja_dva,'procenata poslednja 2 kodona')
#2. nacin
#Ako nismo sigurni, istestiramo print-om
#ali je bitno da na indeksu 6 bude 'A' da bismo 
#dobili bilo kakvu informaciju
print(genetski_kod.count('A',0,6))
procenat_A_prva_dva = (genetski_kod.count('A',0,6) / 6) *100
procenat_A_poslednja_dva = ((genetski_kod.count('A',-6)) / 6)*100
print('A cini',procenat_A_prva_dva,'procenata prva 2 kodona')
print('A cini',procenat_A_poslednja_dva,'procenata poslednja 2 kodona')
