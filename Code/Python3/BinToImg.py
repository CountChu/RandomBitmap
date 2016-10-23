import sys
import getopt
from PIL import Image
import math
import logging

def main ():
    global logger

    print ("")
    print ("======== BinToImg ========")    

    try:
        opts, args = getopt.getopt (sys.argv[1:], "hdcw:")
    except getopt.GetoptError:
        print_usage ()
        sys.exit(2)

    debug = False
    opt_width = 0
    opt_check = False
    for name, value in opts:
        if name == "-h":                # help
            print_usage ()
            sys.exit (0)
        elif name == "-d":              # debug
            debug = True
        elif name == "-w":              # image width
            opt_width = int (value)
        elif name == "-c":              # check size
            opt_check = True           

    if debug:
        loger_init (logging.DEBUG)
    else:
        loger_init (logging.INFO)

    logger.debug (opts)
    logger.debug (args)
    logger.debug ("opt_width = %d" % opt_width)
    if opt_width != 0:
        if opt_width % 8 != 0:
            print ("The width must be 8 times.")
            sys.exit (1)

    if len (args) != 1:
        print_usage ()
        sys.exit (1)

    bin_fn = args [0]
    png_fn = bin_fn + ".png"

    bin_to_img (bin_fn, png_fn, opt_width, opt_check)
    sys.exit (0)    

def print_usage ():
    print ("Usage 1: python3 BinToImage.py -h")
    print ("Usage 2: python3 BinToImage.py -w <width> -d File.bin")
    print ("Usage 3: python3 BinToImage.py -c -w <width> File.bin")    

def loger_init (level):
    global logger

    ch = logging.StreamHandler()
    ch.setFormatter (logging.Formatter("")) # Remove prefix.
    #ch.terminator = "\n\n\n\n"         # No newline character

    logger = logging.getLogger ('MyLogger')
    logger.setLevel(level)    
    logger.addHandler (ch)

def bin_to_img (bin_fn, png_fn, opt_width, opt_check):
    global logger    

    f = open (bin_fn, "rb")
    bytes = f.read()
    print ("The length of the file %s is %d in bytes" % (bin_fn, len(bytes)))
    img_area = 8 * len (bytes)
    print ("Image Area is %d" % img_area)
    if opt_width == 0:
        img_size = int (math.sqrt (img_area))
        img_width = img_size
        img_height = img_size
    else:
        img_width = opt_width
        img_height = math.ceil (img_area / img_width)
    print ("Image Size is (%d, %d)" % (img_width, img_height))
    real_area = img_width * img_height
    print ("Real area is %d x %d = %d" % (img_width, img_height, real_area))
    if opt_check:
        sys.exit (0)
 
    count = 0
    x = 0
    y = 0
    im = Image.new ("RGB", (img_width, img_height), "red")
    pixels = im.load ()
    sys.stdout.write ("y = %d " % y)

    for byte in bytes:

        log = "%02x ---> " % byte

        for idx in range (0, 8):
            count += 1
            r = (byte >> idx) % 2
            log += ("%d" % r)
            if r == 1:
                log += ("(%d, %d)" % (x, y))
                pixels [x, y] = (0, 0, 0)
            else:
                pixels [x, y] = (0xff, 0xff, 0xff)
            x += 1
            if x == img_width:
                x = 0
                y += 1
                sys.stdout.write ("%d " % y)
            log += " "

        logger.debug (log)
    
    print ("")
    logger.debug ("count = %d" % count)
    logger.debug ("x = %d" % x)    
    logger.debug ("y = %d" % y)        

    if count != img_area:
        print ("Error.")
        sys.exit (1)

    im.show ()
    im.save (png_fn)
    print ("Generate the PNG file, %s" % png_fn)

main()
