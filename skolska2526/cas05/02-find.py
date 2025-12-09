#Pretrazujemo karakter T. Hocemo prvo pojavljivanje

kod = 'GCAGCATAGAC'
trazena_baza = 'X'
trazeni_indeks = -1

zavrseno = True
for karakter in kod:
    trazeni_indeks+=1
    if karakter == trazena_baza:
        print(trazeni_indeks)
        zavrseno = False
        break
    
if zavrseno == True:
    print(-1)

#2. nacin bez promenljive zavrseno:
if trazeni_indeks == len(kod)-1:
    print(-1)