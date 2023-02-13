# while (a <5): 
## 5 sayısını istediğiniz değeri yazarsanız o kadar dosya oluşturur

## text yazısını istediğiniz dosya ismi ile değiştirin
## .txt kısmını istediğiniz format ile değiştirin

#bu işlemi çalıştırdığınızda bulunan dizinde şu dosyaları elde edersiniz:
## text1.txt
## text2.txt
## text3.txt
## text4.txt
## text5.txt

#not: uygulamayı çalıştırırken bir dosya içerisinde çalıştırmayı unutmayın
#   dosya hangi dizinde ise oraya oluşturur

'''
**KULLANABİLECEĞİNİZ BAZI DOSYA UZANTILARI**

Microsoft Office Word: .doc, docx
Microsoft Office Excel: .xls, xlsx
Microsoft Office PowerPoint: .ppt, pptx
Microsoft Office Access: .mdb, mdbx
Video: avi, mp4, mkv, wmv, flv, 3gp, dat, mov
Ses: ogg, mp3, wav, mid
Resim: .jpeg, png, bmp, psd
hareketli resim:.gif
E-kitap: .pdf
uygulama yazılımları: exe
sıkıştırılmış dosyalar: .rar, zip, tar, 7z
diğer metin uzantıları: txt, odt, ott, rtf, uot, dic
Website Kodlama Dilleri uzantıları: html, php, aspx, asp
'''


a = 0
while (a < 5):
    a +=1
    file = open(f"text{a}.txt","w")






