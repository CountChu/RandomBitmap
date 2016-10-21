import sys
from PIL import Image
import math


if len (sys.argv) != 2:
	print "Usage: python BinToImage.py File.bin"

bin_fn = sys.argv [1]
png_fn = bin_fn + ".png"

f = open (bin_fn, "rb")
bytes = f.read()
print ("len data = %d" % len(bytes))
img_area = 8 * len (bytes)
print ("img_area = %d" % img_area)
img_size = int (math.sqrt (img_area))
print ("img_size = %d" % img_size)

x = 0
y = 0
im = Image.new ("RGB", (img_size, img_size), "white")
pixels = im.load ()
for byte in bytes:
	byte = ord (byte)
	sys.stdout.write ("%02x " % byte)
	print ("")
	for idx in range (0, 8):
		r = (byte >> idx) % 2
		sys.stdout.write ("%d" % r)
		if r == 1:
			sys.stdout.write ("(%d, %d)" % (x, y))
			pixels [x, y] = (0, 0, 0)
		x += 1
		if x == img_size:
			x = 0
			y += 1
		if y >= img_size:
			break
	if y >= img_size:
		break			
	#print ("")
print ("")

if x != 0:
	print ("Error: x = %d" % x)
	sys.exit (1)
if y != img_size:
	print ("Error: y = %d" % y)
	sys.exit (1)


im.show ()
im.save (png_fn)
sys.exit (0)
