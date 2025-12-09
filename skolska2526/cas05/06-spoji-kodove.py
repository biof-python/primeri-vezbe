fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-sa-ponavljanjem.txt','r')

nadovezan_kod = ''
for linija in fajl:
    # Mogli smo i posle strip da uradimo
    split_linije = linija.split(', ')
    kod = split_linije[0]
    ponavljanja = int(split_linije[1])
    # Mogli smo i
    # for _ range(0,ponavljanja):
    #   nadovezan_kod += kod
    nadovezan_kod += kod*ponavljanja

print(nadovezan_kod)