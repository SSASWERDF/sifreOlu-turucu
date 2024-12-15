import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Kaç karakterlik bir şifre oluşturmak istersiniz"))
sifre = ""
for i in range(sayi):
    sifre = sifre +  random.choice(karakterler)
print(sifre)