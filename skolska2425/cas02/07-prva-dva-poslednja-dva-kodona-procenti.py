my_dna = 'AATTAGCCTATTGTA'
prva_dva_kodona = my_dna[:6]
poslednja_dva_kodona= my_dna[-6:]

udeo_A_u_prva_dva = prva_dva_kodona.count('A')/len(prva_dva_kodona)
udeo_A_u_poslednja_dva_kodona = poslednja_dva_kodona.count('A')/len(poslednja_dva_kodona)

print('A je ' + str(udeo_A_u_prva_dva*100) +'% u prva dva kodona')
print('A je ' + str(udeo_A_u_poslednja_dva_kodona*100)+'% u prva dva kodona')