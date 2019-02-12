print("Menentukan Bilangan Terbesar dari 3 bilangan")
print("--------------------------------------------")

bil1 = input("Masukan bilangan 1 = ")
bil2 = input ("masukan bilangan 2 = ")
bil3 = input ("Masukan bilangan 3 = ")


if bil1 > bil2 and bil1 > bil3:
	print("Bilangan Terbesar dari bilangan tersebut adalah = ",bil1)
	
elif bil2 > bil1 and bil2 > bil3:
	print("Bilangan Terbesar dari bilangan tersebut adalah = ",bil2)

else :
	print("Bilangan Terbesar dari bilangan tersebut adalah = ",bil3)
	
end = input("\nPlease Enter to Exit")


