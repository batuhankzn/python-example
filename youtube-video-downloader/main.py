import pytube

url = input("indirmek istediğiniz video linki: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)