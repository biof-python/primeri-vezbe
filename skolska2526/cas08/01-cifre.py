import re

ulazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/01.txt','r')
izlazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/01-brojevi.txt','w')

#asaga221431141ssfagaga
#221241343
for linija in ulazni_fajl:
    if re.fullmatch('\d+',linija.rstrip()):
        izlazni_fajl.write(linija)
    

ulazni_fajl.close()
izlazni_fajl.close()