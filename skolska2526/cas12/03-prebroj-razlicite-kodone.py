# Ispisati u razliciti_kodoni.txt
# Broj pojavljivanja razlicitih kodona za sve sekvence
# Iz fajlova u folderu sekvence (jedan fajl moze da sadrzi vise sekvenci)
# Na standardni izlaz ispisati sve one kodone koji se pojavljuju vise od granica puta
# Gde se granica unosi kao argument komandne linije:
# python3 03-prebroj-razlicite-kodone.py 12 
# znaci da je granica 12

import re
import os
import sys

def validna_sekvenca(seq):
    return re.fullmatch("([ATGC]{3})+",seq) is not None

input_folder = '/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas12/sekvence'
kodoni_pojavljivanja = {}

for file in os.listdir(input_folder):
    f = open(os.path.join(input_folder,file),'r')
    if not os.path.isfile(os.path.join(input_folder,file)):
        continue
    for seq_line in f:
        seq = seq_line.rstrip()
        if not validna_sekvenca(seq):
            print('Nevalidna sekvenca:' + seq)
            continue

        for kodon in re.findall("[ATGC]{3}",seq):
            kodoni_pojavljivanja[kodon] = kodoni_pojavljivanja.get(kodon,0) + 1

    f.close()

granica = int(sys.argv[1])

with open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas12/razliciti_kodoni.txt','w') as out:
    for k,v in kodoni_pojavljivanja.items():
        out.write(f'{k}:{v}\n')
        if (v > granica):
            print(k)
    