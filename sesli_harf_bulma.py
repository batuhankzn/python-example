#girilen cümle/kelime de kaç adet sesli harf olduğunu sayan program

sesli_harfler = "aeıioöuü"
sayac = 0

kelime = input("Bir kelime girin: ")

for harf in kelime:
    if harf in sesli_harfler:
        sayac +=1

mesaj = print(f"Girdiğiniz {kelime}, kelimesi içinde {sayac} adet sesli harf var")
