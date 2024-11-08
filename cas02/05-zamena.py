#Menjamo A -> T, T->C i C->A
my_dna = 'AATTAGCCTATTGTA'
print(my_dna)
#Zeljeni izlaz: TTCCTGAACTCCGCT

#Ne radi:
zamenjeno_A_i_T = my_dna.replace('A','T')
zamenjeno_T_i_C = zamenjeno_A_i_T.replace('T','C')
zamenjeno_C_i_A = zamenjeno_T_i_C.replace('C','A')

print(zamenjeno_C_i_A)

#Drugi pristup:
zamenjeno_A_i_T = my_dna.replace('A','t')
zamenjeno_T_i_C = zamenjeno_A_i_T.replace('T','c')
zamenjeno_C_i_A = zamenjeno_T_i_C.replace('C','a')

print(zamenjeno_C_i_A.upper())


