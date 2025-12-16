fajl_kodovi = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas06/02-kodovi.txt','r')
fajl_palindormi = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas06/02-palindromi.txt','w')

def isPalindrom(kod):
    pola_duzine = len(kod)//2
    for i in range(0,pola_duzine):
        if kod[i] != kod[-(i+1)]:
            return False
    return True

for kod in fajl_kodovi:        
    if isPalindrom(kod.rstrip()) == True:
        fajl_palindormi.write(kod)

fajl_kodovi.close()
fajl_palindormi.close()