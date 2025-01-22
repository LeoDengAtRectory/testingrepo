alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pt=input("Enter the text you are gonna to encode:")
key=input("Enter the key:")
ks=""
ct=""
for i in range(len(pt)):
	ks+=key[i%len(key)]
for i in range(len(pt)):
	ct+=alph[(alph.index(pt[i])+alph.index(ks[i]))%26]
print("Your encoded text is:"+ct)
