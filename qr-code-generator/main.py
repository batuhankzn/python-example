import pyqrcode

url = input("qr kod için link giriniz: ")
qr_name = input("dosyanın ismini girin: ")

qr_code = pyqrcode.create(url)
qr_code.svg(f'{qr_name}.svg', scale=5)