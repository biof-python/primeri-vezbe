fajl_ulaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/01.txt','r')
fajl_izlaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/01-modifikovan.txt','w')

modifikovan_tekst = "Modifikovali smo 01.txt\n" + fajl_ulaz.read()
fajl_izlaz.write(modifikovan_tekst)

fajl_ulaz.close()
fajl_izlaz.close()