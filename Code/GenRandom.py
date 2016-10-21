
import sys
import RandomGenerator


def main():
    if len (sys.argv) != 2:
        print "Usage: python GenRandom.py File.bin"
        sys.exit(1)

    out_fn = sys.argv [1]
    print ("Output file is %s" % out_fn)
    
    gen_random (out_fn, RandomGenerator.rg1)
    sys.exit(0)

def gen_random (out_fn, random_generator):

    f= open (out_fn, "wb")
    width = 512
    height = 512
    idx = 0
    byte = 0
    for y in range (0, width):
        for x in range (0, height):
            r = random_generator ()
            sys.stdout.write ("%d" % r)
            byte += r << idx
            idx += 1
            if idx == 8:
                f.write (chr(byte))
                print ("")
                print ("%02x" % byte)
                idx = 0
                byte = 0
        print ("")
    f.close()

main()

