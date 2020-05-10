How to use binTHex.py

as -o test.o test.s
objdump -d test.o | python binTHex.py > file_rom.txt
nano file_rom.txt

afterwards in logisim right click ROM, load image -> file_rom.txt
