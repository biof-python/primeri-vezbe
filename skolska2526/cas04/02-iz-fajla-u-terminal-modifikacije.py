f = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas04/01.txt','r')
tekst_za_terminal = 'Ovo je pocetak citanja fajla 01.txt\n'

# tekst_za_terminal = tekst_za_terminal +  f.read().rstrip() je isto sto i:
# rstrip() nam kaze obrisi sve whitespace-ove s kraja
tekst_za_terminal +=  f.read().rstrip()
tekst_za_terminal += '\n'
tekst_za_terminal += "Ovo je kraj citanja fajla 01.txt"

print(tekst_za_terminal)

f.close()