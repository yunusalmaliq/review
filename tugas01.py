def option():
	print("1.desimal ke Biner")
	print("2.desimal ke Octal")
	print("3.biner ke desimal")
	print("4.exit")
	pilihan = int(input("masukan pilihan anda:"))
	return (pilihan)
	
pilihan = True
while(pilihan<4):
	pilihan = option()
	if pilihan == 1:
		print("---------------------------------------------------------")
		x = int(input("masukan angka desimal:"))
		print(bin(x))
		print("---------------------------------------------------------\n")
	elif pilihan == 2:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Desimal: "))
		print (oct(x))
		print("---------------------------------------------------------\n")
	elif pilihan == 3:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Binary: "),2)
		print (x)
		print("---------------------------------------------------------\n")
	else:
		print("good bye")
