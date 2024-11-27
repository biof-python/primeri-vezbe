#Sabiramo prvih n brojeva

n = 10

#1. nacin:
suma = 0
for i in range(1,n+1):
    suma+=i # suma = suma + i
print('Suma je: ' + str(suma))

#2. nacin
j=1
suma = 0
while j<=n:
    suma+=j
    j+=1

print('Suma je: ' + str(suma))