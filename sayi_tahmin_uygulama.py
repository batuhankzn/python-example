'''
1-100 arasında rastegele üretilecek bir sayıyı 
aşağı ve yukarı ifadelerle buldurmaya çalışın

** "random" modülünü kullanın
** 100 üzerinden puanlama yapın her soru 20 puan
** hak bilgisini kullanıcıdan alın her soru belirtilen
    can sayısı üzerinden hesaplansın


'''

import random

sayi = random.randint(1,10)
can = int(input("kaç hak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    
    tahmin = int(input("Sayı giriniz: "))

    if (sayi == tahmin):
        print(f"tebrikler {sayac}. defada bildiniz. Puanınız: {100 - (100/can) * (sayac-1)}")
        break
    elif(sayi > tahmin):
        print("yukarı")
    else:
        print("aşağı")
    
    if(hak == 0):
        print(f"hakkınız bitti tutulan sayı: {sayi}")