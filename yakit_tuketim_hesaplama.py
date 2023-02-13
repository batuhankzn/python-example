#yakıt tüketimi(benzin, dizel) hesaplama

benzinFiyat = 6.69
dizelFiyat = 5.86

ortalamaYakitTuketimi_L = float(input("100 km deki ortalama yakıt tüketiminiz: "))
gidilecekYol_Km = float(input("gidilecek yok kaç km: "))
yakitTipi = input("yakıt tipiniz nedir(dizel/benzin): ") 


toplamYakitTuketimi = gidilecekYol_Km * (ortalamaYakitTuketimi_L / 100)

toplamBenzin = benzinFiyat * toplamYakitTuketimi
toplamDizel = dizelFiyat * toplamYakitTuketimi

if (yakitTipi == "benzin"):
    print(f"Toplam {gidilecekYol_Km} KM yol giderseniz {toplamBenzin} TL yakıt yakarsınız.")
elif (yakitTipi == "dizel"):
    print(f"Toplam {gidilecekYol_Km} KM yol giderseniz {toplamDizel} TL yakıt yakarsınız.")
