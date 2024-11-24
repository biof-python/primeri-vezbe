brojevi = [-1, 24, 35, 99, -2, -3]

#Ova inicijalizacija je jako bitna jer moramo da postavimo maksimum
#na vrednost koja nije veca od svih brojeva u nizu.
#Mogli smo i da postavimo na reicmo "minus beskonacno", ali ovo je dovoljno dobro.
maksimum = brojevi[0]

for broj in brojevi:
    if broj > maksimum:
        maksimum = broj

print('Maksimum naseg niza je broj: ' + str(maksimum))