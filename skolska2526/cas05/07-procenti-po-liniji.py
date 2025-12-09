fajl_ulaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-7.txt','r')
fajl_izlaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-7-procenti.txt','w')

for kod in fajl_ulaz:
    a = (kod.count('A') / len(kod)) * 100
    g = (kod.count('G') / len(kod)) * 100
    c = (kod.count('C') / len(kod)) * 100
    t = (kod.count('T') / len(kod)) * 100

    # Ako hocemo u jednoj liniji: kod.rstrip()
    fajl_izlaz.write(kod + ' -> A: ' + str(a) +'%'
                        + ', G: ' + str(g) +'%'
                        + ', C: ' + str(c)  +'%'
                        + ', T: ' + str(t)  +'%\n')

fajl_izlaz.close()
fajl_ulaz.close()
