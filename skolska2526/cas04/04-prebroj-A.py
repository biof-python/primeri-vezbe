f = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/kodovi.txt','r')
izlaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/prebrojano-A.txt','w')

#f.readlines(): ["ATAGAGAGCTGACT\n","ATTAGCA\n",...]
for linija in f.readlines(): 
    linija_izlaz = linija.rstrip() +': ima ' + str(linija.count('A')) +'A\n'
    izlaz.write(linija_izlaz)

izlaz.close()
f.close()