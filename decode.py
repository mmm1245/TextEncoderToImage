import sys
from PIL import Image
import bitarray

def isSet(value,bit):
	return ((value & (1<<bit)) != 0)



text = ''

ba = bitarray.bitarray()

imin = Image.open("out.png")


width, height = imin.size

bytes = ''

for x in range(width):
	for y in range(height):
		R,G,B,A = imin.getpixel((x,y))

		if(isSet(R,0)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(R,1)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(G,0)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(G,1)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(B,0)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(B,1)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(A,0)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'
		if(isSet(A,1)):
			bytes = bytes + '1'
		else:
			bytes = bytes + '0'

		length = len(bytes)
		if bytes[length-1] == '0' and bytes[length-2] == '0' and bytes[length-3] == '0' and bytes[length-4] == '0' and bytes[length-5] == '0' and bytes[length-6] == '0' and bytes[length-1] == '0' and bytes[length-8] == '0':
			print(bitarray.bitarray(bytes).tobytes().decode('utf-8'))
			sys.exit()
			

print(bitarray.bitarray(bytes).tobytes().decode('utf-8'))
		
		




