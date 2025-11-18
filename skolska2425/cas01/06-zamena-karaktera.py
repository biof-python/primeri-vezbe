genetski_kod = 'ATGCGCTAGCGGCCCGTAAT'
print(genetski_kod)

#1. verzija, greska koja moze da nastane
genetski_kod.replace('G','A')
print(genetski_kod)


print(genetski_kod.replace('G','A'))

promenjeni_kod = genetski_kod.replace('G','A')
print(promenjeni_kod)

genetski_kod = genetski_kod.replace('G','A')
print(genetski_kod)
# genetski_kod = genetski_kod.replace('T','A').replace('C','A')
genetski_kod = genetski_kod.replace('T','A')
genetski_kod = genetski_kod.replace('C','A')
print(genetski_kod)