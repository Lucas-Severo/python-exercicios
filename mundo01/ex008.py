'''
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
'''

dis = float(input('Uma distância em metros: '))
km = dis / 1000
hm = dis / 100
dam = dis / 10
dm = dis * 10
cm = dis * 100
mm = dis * 1000

print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
