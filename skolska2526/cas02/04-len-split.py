ime_prezime = "Miloje Djordje Joksimovic"
print(len(ime_prezime))
ime = ime_prezime[:6]
prezime = ime_prezime[7:]
print(ime)
print(prezime)
ime = ime_prezime.split(' ')[0]
srednje_ime = ime_prezime.split(' ')[1]
prezime = ime_prezime.split(' ')[2]
print(ime)
print(srednje_ime)
print(prezime)