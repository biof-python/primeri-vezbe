# Trazimo kodove sa najivse A,T,G,C
# U slucaju da ih ima vise sa istim brojem 
# ponavljanja vratiti prvi
fajl = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas05/kodovi-8.txt','r')

maksA = -1
najviseA = ''
maksG = -1
najviseG = ''
maksC = -1
najviseC = ''
maksT = -1
najviseT = ''

for kod in fajl:
    a = kod.count('A')
    if a > maksA:
        maksA = a
        najviseA = kod.rstrip()

    g = kod.count('G')
    if g > maksG:
        maksG = g
        najviseG = kod.rstrip()

    c = kod.count('C')
    if c > maksC:
        maksC = c
        najviseC = kod.rstrip()

    t = kod.count('T')
    if t > maksT:
        maksT = t
        najviseT = kod.rstrip()

# U slucaju da je bilo vise a==maksA
# ili t==maksT, c==maksC, g==maksG
# vracamo bilo koji. U drugoj postavci zadatka
# bismo imali dodatnu obradu tog slucaju
# Kada najdemo maksA,maksG,maksC,maksT
# morali bismo jos jednom petljom da prodjemo
# i da upordejujemo trenutni a,g,c,t sa maksimumom
# i onda da nadovezemo kodove za koje vazi
# a==maksA, g==maksG, c==maksC, t==maksT

print('Najvise A ima u: ' + najviseA)
print('Najvise G ima u: ' + najviseG)
print('Najvise C ima u: ' + najviseC)
print('Najvise T ima u: ' + najviseT)

fajl.close()