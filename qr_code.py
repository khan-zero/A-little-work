import random as rm
import qrcode, datetime

# Defineing the YouTube shorts or longs link 
links = ['https://www.youtube.com/watch?v=', 'https://www.youtube.com/shorts/']
link = '' + rm.choice(links)
random_link_list = []

#for shorts
characters = 'qwertyuiopasdfghjklzxcvbnmnQWERTYUIOPASDFGHJKLZXCVBNM1234567890-'
random_link1 = ''.join(rm.choice(characters) for _ in range(10))

#for longs
random_link2 = ''
for _ in range(11):
	temp = ''.join(rm.choice(characters))
	if temp == '-':
		temp = temp.replace('-','=') #in longs there is no "-" but "="
	random_link2 += temp


#chosing one of links
random_link = ''
if 'shorts' in link:
	random_link += link + random_link1
else:
	random_link += link + random_link2

#generating qr img
img = qrcode.make(f'{random_link}')
type(img)

#generating nad saving the random file name
file_name = ''.join(rm.choices(characters, k=5))
x = datetime.datetime.now()
print(f"Link: {random_link}")
img.save(f"{file_name}{x}.png")
print(f"QR code generated succesfully as {file_name}{x}. However the link not works anytime!!")
