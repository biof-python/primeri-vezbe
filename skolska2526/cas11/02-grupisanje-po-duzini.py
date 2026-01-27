"""
ZADATAK 2 - Grupisanje sekvenci po dužini

U folderu "input/" su fajlovi sa DNK sekvencama.

1. Učitati sve sekvence
2. Razvrstati ih u tri grupe:
   - kratke (< 10)
   - srednje (10–50)
   - duge (> 50)
3. Kreirati foldere:
   kratke/, srednje/, duge/
4. Premestiti fajlove u odgovarajući folder
5. Ispisati statistiku:
   kratke: X fajlova (Y %)
   srednje: X fajlova (Y %)
   duge: X fajlova (Y %)
"""

import os
import re

def validna_sekvenca_kodoni(seq):
    return re.fullmatch(r"([ATCG]{3})+", seq) is not None

input_folder = "input"

groups = {
    "kratke": [],
    "srednje": [],
    "duge": []
}

for fname in os.listdir(input_folder):
    path = os.path.join(input_folder, fname)

    if os.path.isfile(path):
        with open(path) as f:
            seq = f.read().strip().upper()

        if not validna_sekvenca_kodoni(seq):
            print(f"{fname}: nevalidna sekvenca ili nije deljiva sa 3")
            continue

        length = len(seq)
        if length < 10:
            groups["kratke"].append(fname)
        elif length <= 50:
            groups["srednje"].append(fname)
        else:
            groups["duge"].append(fname)

total = 0
for v in groups.values():
    total+=len(v)
    
for folder, files in groups.items():
    if not os.path.exists(folder):
        os.mkdir(folder)

    for fname in files:
        src = os.path.join(input_folder, fname)
        dst = os.path.join(folder, fname)
        os.rename(src, dst)

for folder, files in groups.items():
    percent = (len(files) / total) * 100 if total > 0 else 0
    print(f"{folder}: {len(files)} fajlova ({percent:.2f} %)")

