fajl_kodovi = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-5.txt','r')
fajl_ispis = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-vise-3-A.txt','w')
k=3

for linija in fajl_kodovi:
    # Mogli smo i sa count,
    # ovako count zapravo radi
    brojac_A = 0
    for karakter in linija:
        if karakter == 'A':
            brojac_A +=1
    if brojac_A >k:
        fajl_ispis.write(linija)

fajl_ispis.close()
fajl_kodovi.close()
        