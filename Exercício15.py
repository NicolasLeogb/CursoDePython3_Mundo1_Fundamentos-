dia = int(input('Quantos dias alugados?:'))
km = float(input('Quantos quilometros rodados?:'))
#Solução
pf=(dia * 60) + (km * 0.15)
print('O total a pagar é de R$ {}'.format (pf))