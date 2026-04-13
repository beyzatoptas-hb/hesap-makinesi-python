print("Hesap Makinesi")

sayi1 = float(input("1. sayıyı gir: "))
sayi2 = float(input("2. sayıyı gir: "))

print("İşlemler: + - * /")
islem = input("İşlem seç: ")

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
    else:
        sonuc = "Sıfıra bölünemez!"
else:
    sonuc = "Geçersiz işlem!"

print("Sonuç:", sonuc)