import re

def ispisi_grupu(match, i):
    if i<0 or i > len(match.groups()):
        return
    print('Cela grupa je: ' + match.group(i))
    print('Pocetak grupe je indeks: ' +str(match.start(i)))
    print('Kraj grupe je indeks: ' + str(match.end(i)))

genetski_kod = 'ATAGAGAGACAGTAGA'
match = re.search('A(G*)(AG)?A',genetski_kod)

# ispisi_grupu(match,0)
# ispisi_grupu(match,1)
# ispisi_grupu(match,2)
# ispisi_grupu(match,-3)

for x in match.groups():
    print(x)

