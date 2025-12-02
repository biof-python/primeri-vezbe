# A->T, T->G, G->A
#   ATGCTGATGATA 
#-> TGACGATGATGT

#Podzadatak: A->T
genetski_kod = 'ATGCTGATGATA'
print('Pocetni kod:', genetski_kod)
genetski_A_u_T = genetski_kod.replace('A','T')
print('Kada zamenimo A->T dobijamo:',genetski_A_u_T)

# Originalan zadatak:
# Problem je ako radimo replace('A','T'),
# pa onda replace('T','G') jer ne postoji razlika
# izmedju novog i originalnog 'T'.
# Resenje: Uradimo replace ('A','t') i posle
# replace('t','T'). Isto to i za ostale zamene
print('Sada radimo A->T, T->G, G->A')
novi_genetski_kod = genetski_kod.replace('A','t')
novi_genetski_kod = novi_genetski_kod.replace('T','g')
novi_genetski_kod = novi_genetski_kod.replace('G','a')
print('Novi genetski kod je:', novi_genetski_kod.upper())

#2. nacin:
novi_genetski_kod = genetski_kod.replace('A','t').replace('T','g').replace('G','a')
print('Novi genetski kod je:', novi_genetski_kod.upper())