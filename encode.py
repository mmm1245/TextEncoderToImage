import sys
from PIL import Image
import bitarray

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)



text = ''

for i in range(len(sys.argv)-1):
	if text == '':
		text = sys.argv[i+1]
	else:
		text = text + ' ' + sys.argv[i+1]

print('encoding ' + text)

ba = bitarray.bitarray()
text += "\00"
ba.frombytes(text.encode('utf-8'))
print(ba)

imin = Image.open("source.jpeg")

imin = imin.convert('RGBA')

width, height = imin.size

bit = 0

for x in range(width):
	for y in range(height):
		R,G,B,A = imin.getpixel((x,y))


		if ba.tolist()[bit]:
			R = set_bit(R, 0)
		else:
			R = clear_bit(R, 0)
		bit = bit+1

		if ba.tolist()[bit]:
			R = set_bit(R, 1)
		else:
			R = clear_bit(R, 1)
		bit = bit+1

		if ba.tolist()[bit]:
			G = set_bit(G, 0)
		else:
			G = clear_bit(G, 0)
		bit = bit+1

		if ba.tolist()[bit]:
			G = set_bit(G, 1)
		else:
			G = clear_bit(G, 1)
		bit = bit+1
		if ba.tolist()[bit]:
			B = set_bit(B, 0)
		else:
			B = clear_bit(B, 0)
		bit = bit+1

		if ba.tolist()[bit]:
			B = set_bit(B, 1)
		else:
			B = clear_bit(B, 1)
		bit = bit+1

		if ba.tolist()[bit]:
			A = set_bit(A, 0)
		else:
			A = clear_bit(A, 0)
		bit = bit+1

		if ba.tolist()[bit]:
			A = set_bit(A, 1)
		else:
			A = clear_bit(A, 1)
		bit = bit+1
		
		imin.putpixel((x,y),(R,G,B,A))
		if(len(ba.tolist()) <= bit):
			print("end")
			imin.save("out.png")
			sys.exit()



imin.save("out.png")








