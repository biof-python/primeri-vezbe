ulaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/potencijalni-kodovi.txt','r')
izlaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/validacija-kodova.txt','w')

for linija in ulaz.readlines():
    linija_bez_novog_reda = linija.rstrip() 
    linija_izlaz = linija_bez_novog_reda
    if linija_bez_novog_reda.count('A') + linija_bez_novog_reda.count('G') + linija_bez_novog_reda.count('C') + linija_bez_novog_reda.count('T') == len(linija_bez_novog_reda):
        linija_izlaz+= " je validan\n"
    else:
        linija_izlaz+= " nije validan\n"
    izlaz.write(linija_izlaz)

ulaz.close()
izlaz.close()