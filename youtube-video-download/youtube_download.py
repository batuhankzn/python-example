import pytube

#kullanıcıdan video linki
url = input("enter video url: ")

#boş bırakıyoruz çıktıyı dizine gönderecek
path = ""

#pytube kütüphanesi
pytube.YouTube(url).streams.get_highest_resolution().download(path)