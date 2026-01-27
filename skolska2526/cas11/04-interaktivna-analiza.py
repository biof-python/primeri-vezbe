"""
ZADATAK 4 – Interaktivna analiza sekvenci

Korisnik unosi:
- ime foldera sa sekvencama
- minimalnu dužinu sekvence

1. Učitati fajlove
2. Ignorisati sekvence kraće od minimalne dužine
3. Za svaku validnu sekvencu (ATCG + deljiva sa 3):
   - izračunati procenat A, T, C, G
4. Upisati rezultate u fajl "analiza.txt"
"""

import os
import re

def validna_sekvenca_kodoni(seq):
    return re.fullmatch(r"([ATCG]{3})+", seq) is not None

folder = input("Unesite ime foldera: ").strip()
min_len = int(input("Unesite minimalnu dužinu sekvence: "))

with open("analiza.txt", "w") as out:
    out.write("fajl\tA%\tT%\tC%\tG%\n")

    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)

        if os.path.isfile(path):
            with open(path) as f:
                seq = f.read().strip().upper()

            if not validna_sekvenca_kodoni(seq):
                continue

            if len(seq) < min_len:
                continue

            total = len(seq)
            a = len(re.findall(r"A", seq)) / total * 100
            t = len(re.findall(r"T", seq)) / total * 100
            c = len(re.findall(r"C", seq)) / total * 100
            g = len(re.findall(r"G", seq)) / total * 100

            out.write(f"{fname}\t{a:.2f}\t{t:.2f}\t{c:.2f}\t{g:.2f}\n")

