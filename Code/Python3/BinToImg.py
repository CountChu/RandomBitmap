import sys
from PIL import Image
import math
import logging

def main ():
    global logger

    loger_init (logging.INFO)    
    #loger_init (logging.DEBUG)    

    print ("")
    print ("======== BinToImg ========")    

    if len (sys.argv) != 2:
        print ("Usage: python BinToImage.py File.bin")


    bin_fn = sys.argv [1]
    png_fn = bin_fn + ".png"

    bin_to_img (bin_fn, png_fn)
    sys.exit (0)    

def loger_init (level):
    global logger

    ch = logging.StreamHandler()
    ch.setFormatter (logging.Formatter("")) # Remove prefix.
    #ch.terminator = "\n\n\n\n"         # No newline character

    logger = logging.getLogger ('MyLogger')
    logger.setLevel(level)    
    logger.addHandler (ch)

def bin_to_img (bin_fn, png_fn):
    global logger    

    f = open (bin_fn, "rb")
    bytes = f.read()
    print ("The length of the file %s is %d in bytes" % (bin_fn, len(bytes)))
    img_area = 8 * len (bytes)
    print ("Image Area is %d" % img_area)
    img_size = int (math.sqrt (img_area))
    print ("Image Size is (%d, %d)" % (img_size, img_size))

    x = 0
    y = 0
    im = Image.new ("RGB", (img_size, img_size), "white")
    pixels = im.load ()
    sys.stdout.write ("y = %d " % y)
    for byte in bytes:
        #logger.debug ("byte = %d" % byte)
        #byte = ord (byte)
        log = "%02x ---> " % byte
        for idx in range (0, 8):
            r = (byte >> idx) % 2
            log += ("%d" % r)
            if r == 1:
                log += ("(%d, %d)" % (x, y))
                pixels [x, y] = (0, 0, 0)
            x += 1
            if x == img_size:
                x = 0
                y += 1
                sys.stdout.write ("%d " % y)
            if y >= img_size:
                break
            log += " "
        if y >= img_size:
            break           
        logger.debug (log)
    print ("")

    if x != 0:
        print ("Error: x = %d" % x)
        sys.exit (1)
    if y != img_size:
        print ("Error: y = %d" % y)
        sys.exit (1)

    im.show ()
    im.save (png_fn)
    print ("Generate the PNG file, %s" % png_fn)

main()
