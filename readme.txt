How to use binTHex.py

as -o test.o test.s
objdump -d test.o | python trBinaryHexa.py > file_rom.txt
nano file_rom.txt

then in logisim right click ROM, load image -> file_rom.txt