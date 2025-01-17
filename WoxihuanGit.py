alp = "abcdefghijklmnopqrstuvwxyz"


encrypted = ''

x = input("Gae woa text I should encrypt or some goushi: ")
y = int(input("shift how much"))


for jamal in x:
	encrypted+=alp[(alp.index(jamal)+y)%26]


	


print(encrypted)

