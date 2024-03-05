import random

print("zar oyununa hosgeldiniz1")

a = input("1. oyuncunun ismini giriniz: ")
b = input("2. oyuncunun ismini giriniz: ")

print(f"{a} in sırası.")

random_number = random.randint(0, 7)
random_number1 = random.randint(0, 7)

print(a,"'ın 1.zarı =",random_number)
print(a,"'ın 2.zarı =",random_number1)
print(a,"'ın attığı zarların toplamı:  =" ,random_number + random_number1)
print("****************")
print(f"{b} ın sırası.")

random_number2 = random.randint(0, 7)
random_number3 = random.randint(0, 7)


print(b,"'ın 1.zarı =",random_number2)
print(b,"'ın 2.zarı =",random_number3)
print(b,"'ın attığı zarların toplamı:  =" ,random_number2 + random_number3)
if random_number+ random_number1 >random_number2+ random_number3:
    print(f"{a} KAZANDI!")

elif random_number+ random_number1 == random_number2 + random_number3:
    print("BERABERE")

else:
    print(f"{b} KAZANDI")    
