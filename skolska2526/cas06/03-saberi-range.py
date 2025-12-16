#Sabira cele brojeve u intervalu [a,b]
def saberi_range(a,b):
    # suma = 0
    # for i in range(a,b+1):
    #     suma +=i
    # return suma
    suma = 0
    i = a
    while (i<=b):
        suma += i
        i+=1
    return suma
# Optimalno resenje: 
# return (b*(b+1))//2 - (a*(a+1))//2

print(saberi_range(2,5))