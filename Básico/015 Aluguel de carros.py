km = float(input("Digite a quantidade de KM percorridos: "))
dia = int(input("Dias alugados: "))
pfinal = (km*0.15) + (dia*60)
print ("O total a pagar é de R${:.2f}".format(pfinal))