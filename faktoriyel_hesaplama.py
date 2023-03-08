#faktoriyel hesaplama fonksiyonu

def faktoriyel(x):
    if x==1:
        return 1
    
    return x* faktoriyel(x-1)


sonuc = faktoriyel(5)

print(sonuc)