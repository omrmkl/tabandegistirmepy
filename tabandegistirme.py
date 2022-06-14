sonuc = ""
basamak = 0
top = 0
sayac = 0
while 1 == 1:
    print("*****TABAN DEĞİŞTİRME MAKİNASI*****\n"
          "Onluk tabandan ikilik tabana geçiş için 1 sayısını girin.\n"
          "İkilik tabandan onluk tabana geçiş için 2 sayısını girin.\n"
          "Çıkmak için herhangi bir sayı girin.")
    secim = int(input("--->"))
    if secim == 1:
        sayı = int(input("Değiştirmek istediğiniz sayıyı girin\n--->"))
        if sayı == 0:
            print("Değişim sonucu : 0\n")
        while sayı >= 1:
            kalan = sayı % 2
            sayı = sayı // 2
            sonuc = str(kalan) + sonuc
        print("Değişim sonucu :\n", sonuc)
        sonuc=""
    elif secim == 2:
        b = 1
        while b == 1:
            a = 1
            sayı = int(input("Değiştirmek istediğiniz sayıyı girin\n--->"))
            sayı3 = sayı
            while sayı3 > 0:
                test = sayı3 % 10
                if test == 1 or test == 0:
                    sayı3 = sayı3 // 10
                else:
                    print("Hatalı giriş!")
                    sayı3 = 0
                    a = 0
            while a == 1:
                sayı2 = sayı
                while sayı2 > 0:
                    sayı2 = sayı2 // 10
                    basamak += 1
                for i in range(basamak):
                    sonbasamak = sayı % 10
                    top = (2 ** i) * sonbasamak + top
                    sayı = sayı // 10
                print("Değişim sonucu :", top)
                b = 0
                a = 0
            top = 0
    else:
        break
