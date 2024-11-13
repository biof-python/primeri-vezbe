fajl_za_ucitavanje = open('01.txt','r')
fajl_za_ispis = open('ispis.txt','w')

ucitani_tekst = fajl_za_ucitavanje.read()
tekst_za_ispis = 'Modifikujem ucitani tekst: \n' + ucitani_tekst
fajl_za_ispis.write(tekst_za_ispis)