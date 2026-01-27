"""
ZADATAK 5 – Rečnik: ime fajla -> broj validnih kodona

U folderu "sekvence/" nalaze se fajlovi sa DNK sekvencama.

1. Učitati sve fajlove
2. Za svaki fajl:
   - proveriti da li je sekvenca validna (ATCG + deljiva sa 3)
   - podeliti sekvencu na kodone (po 3)
   - prebrojati koliko ima validnih kodona
3. Formirati rečnik:
   ime_fajla -> broj_validnih_kodona
4. Ispisati rečnik na ekran
5. Sačuvati rečnik u fajl "kodoni_po_fajlu.txt"
"""

import os
import re

def validna_sekvenca_kodoni(seq):
    return re.fullmatch(r"(?:[ATCG]{3})+", seq) is not None

folder = "sekvence"
recnik = {}

for fname in os.listdir(folder):
    path = os.path.join(folder, fname)

    if os.path.isfile(path):
        with open(path) as f:
            seq = f.read().strip().upper()

        if not validna_sekvenca_kodoni(seq):
            print(f"{fname}: nevalidna sekvenca ili nije deljiva sa 3")
            continue

        kodoni = re.findall(r"[ATCG]{3}", seq)
        recnik[fname] = len(kodoni)

with open("kodoni_po_fajlu.txt", "w") as out:
    for k, v in recnik.items():
        out.write(f"{k}: {v}\n")

print("Rečnik ime_fajla -> broj_validnih_kodona:")
print(recnik)

