
d = {'mleko':120, 'brasno':80, 'jabuke':150 }

print(d)
# Hocemo da saberemo sve cene:
suma = 0
d['jogurt'] = 185
for kljuc, vrednost in d.items():
    print(kljuc)
    suma += vrednost

print(suma)

print('Vrednost jabuke je: ' + str(d['jabuke']))
d['jabuke']=160
print('Nova vrednost jabuke je: ' + str(d['jabuke']))

for kljuc in d.keys():
    print('kljuc: ' + kljuc + ', vrednost: ' + str(d[kljuc]))