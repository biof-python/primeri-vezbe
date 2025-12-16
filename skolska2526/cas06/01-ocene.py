poeni_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas06/01-poeni.txt','r')
ocene_fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas06/01-ocene.txt','w')

def poeni_u_ocenu(poeni):
    # ocena = 5   
    # if poeni >= 91:
    #     ocena = 10
    # elif poeni >= 81:
    #     ocena = 9
    # elif poeni >= 71:
    #     ocena = 8
    # elif poeni >= 61:
    #     ocena = 7
    # elif poeni >= 51:
    #     ocena =6
    # else:
    #     ocena = 5
    # return ocena

    # 2. nacin odmah return, bez promenljive
    # Nema potrebere za elif jer return prekida sve
    if poeni >= 91:
        return 10
    if poeni >= 81:
        return 9
    if poeni >= 71:
        return 8
    if poeni >= 61:
        return 7
    if poeni >= 51:
        return 6
    return 5

for linija in poeni_fajl:
    ime = linija.split(', ')[0]
    poeni = linija.split(', ')[1]
    poeni = float(poeni)
    ocena = poeni_u_ocenu(poeni)
    ocene_fajl.write(ime + ', ' + str(ocena) +'\n') 


poeni_fajl.close()
ocene_fajl.close()