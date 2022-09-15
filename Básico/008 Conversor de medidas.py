from statistics import median

metro = float(input("Digite uma distância em metros: "))
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000
print("Kilômetro: {:.0f} \nHectômetro: {:.0f} \nDecâmetro: {:.0f} \nDecímetro: {:.0f} \nCentímetro: {:.0f} \nMilímetro: {:.0f}".format(km,hm,dam,dm,cm,mm))
