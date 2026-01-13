# Iz ulaznog fajla da ipsisemo na izlazni:
# Kodove validne koji pocinju sa ATG a zavrsavaju se sa TGA ili TAG
import re

ulazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/05.txt','r')
izlazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/05-odgovarajuci.txt','w')

for linija in ulazni_fajl:
    if re.fullmatch('^(ATG)([ATGC]{3})*((TAG)|(TGA))$',linija.rstrip()):
        izlazni_fajl.write(linija)


ulazni_fajl.close()
izlazni_fajl.close()