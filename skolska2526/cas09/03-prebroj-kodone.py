def inicijalizuj_recnik():
    d = {}
    skup = ['A','T','G','C']
    for x in skup:
        for y in skup:
            for z in skup:
                d[x+y+z] = 0
    return d

def prebroj_kodone(genetski_kod):
    d = inicijalizuj_recnik()    
    for i in range(0,len(genetski_kod),3):
        kodon = genetski_kod[i:i+3]
        d[kodon] += 1

    return d

genetski_kod = 'ATGCATAGATAGTATACATAC'
print(prebroj_kodone(genetski_kod))
