t=int(input("tell the temperature:-"))
if t<0:
    print("frezzing cold")
elif t>=0 and t<10:
    print("very cold")
elif t>=10 and t<20:
    print("cold")
elif t>=20 and t<30:
    print("pleasent")
elif t>=30 and t<40:
    print("hot")
else:
    print("temperature with very hot")        
    