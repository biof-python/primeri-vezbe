"""
ZADATAK 3 - Brojanje kodona

Korisnik unosi putanju do foldera sa sekvencama.

1. Učitati sve fajlove
2. Iz svake sekvence izdvojiti kodone (po 3 nukleotida)
3. Prebrojati koliko se puta svaki kodon pojavljuje
4. Sačuvati rezultate u fajl "kodoni.txt"
5. Validacija: sekvenca mora imati samo A,T,C,G i biti deljiva sa 3
"""

import os
import re

def validna_sekvenca_kodoni(seq):
    return re.fullmatch(r"(?:[ATCG]{3})+", seq) is not None

folder = input("Unesite putanju do foldera sa sekvencama: ").strip()
kodoni = {}

for fname in os.listdir(folder):
    path = os.path.join(folder, fname)

    if os.path.isfile(path):
        with open(path) as f:
            seq = f.read().strip().upper()

        if not validna_sekvenca_kodoni(seq):
            print(f"{fname}: nevalidna sekvenca ili nije deljiva sa 3")
            continue

        for kodon in re.findall(r"[ATCG]{3}", seq):
            kodoni[kodon] = kodoni.get(kodon, 0) + 1

with open("kodoni.txt", "w") as out:
    for k, v in sorted(kodoni.items()):
        out.write(f"{k}: {v}\n")
