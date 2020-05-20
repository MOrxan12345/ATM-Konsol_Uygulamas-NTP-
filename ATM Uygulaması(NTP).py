from time import sleep

class ATM():

    def __init__(self,para):
        self.para = para

    def paraYatir(self,miktar):
        if miktar <= 500:
            self.para += miktar
        else:
            print("Maksimum yatırabileceğiniz para miktarı: 500Tl")

    def paraCek(self,miktar):
        if miktar <= 1000:
            if self.para - miktar > 0:
                self.para -= miktar
            else:
                print("Bu miktarı çekmek için yeterli bakiyeniz yoktur.")
        else:
            print("Maksimum 1000Tl çekebilirsiniz")

    def paraSorgula(self):
        return f" Bakiyeniz: {self.para} Tl"

if __name__ == '__main__':

    b = ATM(0)
    print("""
         ___________________________________
        |   ATM Uygulamasına Hoş Geldiniz   | 
        |___________________________________|""")
    while True:
        print("""
         ___________________________________
        |                                   |
        | Seçim Ediniz: (1) Bakiye Sorğula  |
        |               (2) Para Yatır      |
        |               (3) Para Çek        |
        |               (exit) Çıkış        |
        |___________________________________|
        """)

        secim = input(">>>")

        if secim =="exit":
            print("Uygulama sonlanıyor...")
            sleep(1)
            break

        elif secim == "1":
            print(b.paraSorgula())

        elif secim == "2":
            miktar = float(input("Yatırılacak para miktarını giriniz: "))
            print("İşlem yapılıyor....")
            sleep(2)
            b.paraYatir(miktar)
            print(b.paraSorgula())

        elif secim == "3":
            print("İşlem yapılıyor....")
            miktar = float(input("Çekilecek para miktarını giriniz: "))
            sleep(2)
            b.paraCek(miktar)
            print(b.paraSorgula())

        else:
            print("Yalnış seçim! Lütfen doğru seçim ediniz.")

