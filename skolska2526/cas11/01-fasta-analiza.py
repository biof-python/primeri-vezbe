"""
ZADATAK 1 - Analiza FASTA fajlova u folderu

U folderu "sekvence/" nalaze se tekstualni fajlovi.
Svaki fajl sadrži jednu DNK sekvencu u jednom redu.

1. Pročitati sve fajlove iz foldera "sekvence/"
2. Za svaki fajl:
   - proveriti da li sekvenca sadrži samo A, T, C, G
   - proveriti da li je dužina deljiva sa 3 (kodoni)
   - izračunati procenat GC sadržaja
3. Kreirati folder "rezultati/"
4. U fajl "gc_rezultati.txt" upisati:
   ime_fajla  duzina  GC_procenat
"""

import os
import re

def validna_sekvenca_kodoni(seq):
    return re.fullmatch(r"([ATCG]{3})+", seq) is not None

def gc_content(seq):
    gc = len(re.findall(r"[GC]", seq))
    return (gc / len(seq)) * 100

input_folder = "sekvence"
output_folder = "rezultati"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

out_path = os.path.join(output_folder, "gc_rezultati.txt")

with open(out_path, "w") as out:
    out.write("fajl\tduzina\tGC_procenat\n")

    for fname in os.listdir(input_folder):
        path = os.path.join(input_folder, fname)

        if os.path.isfile(path):
            with open(path) as f:
                seq = f.read().strip().upper()

            if not validna_sekvenca_kodoni(seq):
                print(f"{fname}: nevalidna sekvenca ili nije deljiva sa 3")
                continue

            gc = gc_content(seq)
            out.write(f"{fname}\t{len(seq)}\t{gc:.2f}\n")

