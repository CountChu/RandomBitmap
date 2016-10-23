
import logging
import sys
import RandomGenerator

def main():
    global logger

    loger_init (logging.INFO)
    #loger_init (logging.DEBUG)

    print ("")
    print ("======== GenRandom ========")

    if len (sys.argv) != 2:
        print ("Usage: python GenRandom.py File.bin")
        sys.exit(1)

    out_fn = sys.argv [1]
    print ("Output file is %s" % out_fn)
    
    gen_random (out_fn, RandomGenerator.rg1)
    sys.exit(0)

def loger_init (level):
    global logger

    ch = logging.StreamHandler()
    ch.setFormatter (logging.Formatter("")) # Remove prefix.
    #ch.terminator = "\n\n\n\n"         # No newline character

    logger = logging.getLogger ('MyLogger')
    logger.setLevel(level)    
    logger.addHandler (ch)

def gen_random (out_fn, random_generator):
    global logger    

    f= open (out_fn, "wb")

    width = 512
    height = 512
    print ("Image Size is (%d, %d)" % (width, height))    
    
    idx = 0
    byte = 0
    log = ""
    for y in range (0, width):
        for x in range (0, height):
            r = random_generator ()
            log += ("%d" % r)
            byte += r << idx
            idx += 1
            if idx == 8:
                byte_list = []
                byte_list.append (byte)
                f.write (bytes(byte_list))
                log += " ---> %02x\n" % byte
                idx = 0
                byte = 0
        logger.debug (log)
    f.close()
    print ("Generate the file, %s" % out_fn)    

main()