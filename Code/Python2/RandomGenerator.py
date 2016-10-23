import random

#
# The rg1() is Python random generator.
#

def rg1 ():
	return random.randint (0, 1)	

#
# The rg2() is a user customized random generator.
#

def rg2 ():
	r = (lcg() >> 4) % 2
	return r

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 1140671485
    c = 128201163
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    return rand

seedLCG(1)

