real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = real / 5.25
euro = real / 5.35
print ("Com R$ {} você pode comprar US$ {:.2f} e £ {:.2f} ".format(real,dolar,euro))
