fajl_reci = open('reci.txt')
fajl_palindromi = open('palindromi.txt','w')

broj_palindroma = 0
for linija in fajl_reci:
    rec = linija.rstrip()
    duzina_reci = len(rec)
    
    #pretpostavimo da je rec palindrom
    jeste_palindrom = True
    for i in range(0,duzina_reci//2):
        if rec[i] != rec[-i-1]: #rec[duzina_reci - i -1]
            jeste_palindrom = False
    
    if jeste_palindrom == True:
        fajl_palindromi.write(rec + '\n')
        broj_palindroma +=1

print('Broj palindroma je: ' + str(broj_palindroma))