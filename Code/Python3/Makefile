clean:
	rm -f *.bin
	rm -f *.png
	rm -f *.pyc

test1:
	python3 GenRandom.py ../../Test/Random.bin
	python3 BinToImg.py ../../Test/Random.bin

test2:
	python3 BinToImg.py BinToImg.py	

test3:
	python3 BinToImg.py ../../Test/Test.pdf	

test4:
	python3 BinToImg.py -d ../../Test/Test.txt	
	python3 BinToImg.py -w 24 -d ../../Test/Test.txt

test5:
	python3 BinToImg.py -w 6000 ../../Test/BIOS.rom
	python3 BinToImg.py -w 6000 ../../Test/SPI0.bin	
	python3 BinToImg.py -w 6000 ../../Test/SPI1.bin	