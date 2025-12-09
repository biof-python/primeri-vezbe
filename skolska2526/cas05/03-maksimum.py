a = [-1, -5, 0, 100, -3, 40]

# Ako je niz prazan a[0] ne postoji
# To bi zahtevalo dodatnu proveru, ali
# ovde je necemo raditi
# if len(a) == 0:
#  ...
maks = a[0]
for element in a:
    if element >= maks:
        maks = element

print("Maksimum je " + str(maks))