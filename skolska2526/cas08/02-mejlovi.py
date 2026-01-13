import re

ulazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/02.txt','r')
izlazni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas08/02-mejlovi.txt','w')

# asfia92
# miloje.joksimov2i_c@matf.bg.ac.rs
for linija in ulazni_fajl:
    if re.fullmatch('[\d\w\W_.]+@\w+.\w+',linija.rstrip()):
        izlazni_fajl.write(linija)
        

ulazni_fajl.close()
izlazni_fajl.close()