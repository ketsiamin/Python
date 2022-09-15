from math import hypot
cato = float(input("Qual a comprimento do cateto oposto: "))
cata = float(input("Qual o comprimento do cateto adjacente: "))
hi = hypot (cato,cata)
print ("A hipotenusa vai medir {:.2f}".format(hi))