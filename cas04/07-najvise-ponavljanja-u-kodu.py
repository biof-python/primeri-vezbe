kodovi = open('kodovi-07.txt')
najvise_ponavljanja = open('najvise_ponavljanja.txt','w')

#Posto imamo uvek bar 0 ponavljanja u kodu,
#mozemo da incijalizujemo na -1
maxA = -1
kodMaxA = ''
maxG = -1
kodMaxG = ''
maxC = -1
kodMaxC = ''
maxT = -1
kodMaxT = ''

for kod in kodovi:
    if kod.count('A') > maxA:
        maxA = kod.count('A')
        kodMaxA = kod
    
    if kod.count('G') > maxG:
        maxG = kod.count('G')
        kodMaxG = kod
    
    if kod.count('C') > maxC:
        maxC = kod.count('C')
        kodMaxC = kod
    
    if kod.count('T') > maxT:
        maxT = kod.count('T')
        kodMaxT = kod

najvise_ponavljanja.write('Najvise A, ' + str(maxA) +' ima kod '+kodMaxA)
najvise_ponavljanja.write('Najvise G, ' + str(maxG) +' ima kod '+kodMaxG)
najvise_ponavljanja.write('Najvise C, ' + str(maxC) +' ima kod '+kodMaxC)
najvise_ponavljanja.write('Najvise T, ' + str(maxT) +' ima kod '+kodMaxT)