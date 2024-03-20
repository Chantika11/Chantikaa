bilangan = int (input("masukan bilangan yang ingin dikonversi"))

konversi1 = bin (bilangan) [2:]
konversi2 = hex (bilangan)
konversi3 = oct (bilangan)

print ("bilangan Biner \t\t: ", konversi1. zfill(8))
print ("bilangan Hexadecimal \t:", konversi2)
print ("bilangan Octal \t\t ", konversi3)