fajl_poeni = open('poeni.txt','r')
fajl_ocene = open('ocene.txt','w')

for linija in fajl_poeni:
    podeljena_linija = linija.split(',')
    ime_i_prezime = podeljena_linija[0]
    poeni = int(podeljena_linija[1])
    ocena = 5
    if poeni > 50 and poeni <= 60:
        ocena = 6
    if poeni > 60 and poeni <= 70:
        ocena = 7
    if poeni > 70 and poeni <=80:
        ocena =8
    if poeni > 80 and poeni <= 90:
        ocena =9
    if poeni > 90:
        ocena = 10
    
    fajl_ocene.write(ime_i_prezime + ': ' + str(ocena)+'\n')