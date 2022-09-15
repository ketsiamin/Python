l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
m2 = l*a
tinta = m2/2
print ("Sua parede tem dimensão de {} X {} e sua área é de {}m²".format(l,a,m2))
print ("Para pintar essa parede, você precisará de {:.2f}l de tinta".format(tinta))