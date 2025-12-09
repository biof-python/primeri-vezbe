# Ispisujemo vocke koje pocinju sa A
voce = ['Ananas', 'Banana', 'Jabuka','Avokado','Lubenica']

vockice_na_A = ''
for vocka in voce:
    #Mogli smo da koristimo i vocka.startswith()
    if vocka[0] == 'A' or vocka[0] == 'a':
        vockice_na_A += vocka +', '

# Zbog razmaka je [:-2], a ne [:-1] 
vockice_na_A = vockice_na_A[:-2]
print('Vocke koje pocinju sa A su: ' + vockice_na_A)

        