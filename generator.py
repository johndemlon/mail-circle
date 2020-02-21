import string
import random

ltrs = string.ascii_letters
cntr = 1

def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))
text_file = open("emails.txt", "w")
nmml = input("How many emails do you want ?	")
nmcr = input("How many charecters do you want ?	")

for i in range(0,int(nmml)):
	gnrtd1 = str(cntr)+"-"
	print(gnrtd1)
	#gnrtd = random_char(5)
	gnrtd2 = str(random_char(int(nmcr)))+"@john9119.33mail.com"
	print(gnrtd2.lower())
	text_file.write("""gnrtd1"""+gnrtd2.lower()+'\n')
	cntr = cntr+1

text_file.close()

print("By The Fake 8")
print("https://paypal.me/demlon")
