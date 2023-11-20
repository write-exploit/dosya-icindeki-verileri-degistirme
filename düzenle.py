import os
from termcolor import colored # pip install termcolor
import signal # pip install python-signal
import sys 
#====================
def __signal_handler(sig,frame):# fonksiyonun başına __ işareti koyduğumuzda kullanıcı modülü kullanırken bu fonksiyonlara ulaşamaz yani gizli fonksiyon olur
    print("bye...") 
    sys.exit(0) # ctrl+c'ye basıldı ise çıkış yapıyoruz
signal.signal(signal.SIGINT, __signal_handler) 
# ctrl+c'ye basıldıgında kod hata çıktısı firlatıyor biz burada hata çıktısını tutucaz ve yerine yukarıdaki bye...  mesajını yazdırıcaz
#=====================
def __Terminal_Temizle(): # gizli fonksiyon (belirli yerlerde bu fonksiyonu çağırarak terminalimizi temizliycez)
    if os.name == 'nt': # işletim sistemi windows ise cls komutu çalışır değilse clear komutu çalışır
        os.system("cls")
    else: 
        os.system("clear")
#=====================
# eski : değiştirilecek değer
# yeni : eski değer yerine yazılacak değer

# dosya_yolu : __file__ değerinin girilmesi lazım 
# bu değer sayesinde modül hangi dosyada import edildiyse o dosyanın yolu bize gelecektir
# uzun bir şekilde dosya yolunu belirtmekten cok daha faydalı
def main(eski,yeni,dosya_yolu):

    with open(dosya_yolu,"r",encoding="utf8") as dosya:
        içerik = dosya.read()
        if eski not in içerik:
            print("mevcut olmayan bir içerik girdiniz")
        else:    
            __Terminal_Temizle()
            # ----isterseniz uyarı kısmını kaldırabilirsiniz----
            print(colored("İŞLEME DEVAM ETMEK İSTEDİĞİNİZDEN EMİNMİSİNİZ e/h\n","red"))
            print("silinecek değer :")
            print(eski)
            print("\nyerine gelecek değer :")
            print(yeni,"\n")
            cevap = input().lower()
            if cevap == 'e':
                dosya = içerik.replace(eski,yeni) # replace fonksiyonu sola verilen değeri sağdaki değer ile değiştirir
                with open(dosya_yolu,"w",encoding="utf8") as yeni_içerik:
                    yeni_içerik.write(dosya)
                    __Terminal_Temizle()
                    print("====içerik değiştirildi====")
                    print("eğer dosyanızda istemediğiniz bir değişiklik oldu ise ctrl+z ile işlemi geri alabilirsiniz")
                    print("başka bir değişiklik yapmak istemiyorsanız modülü kaldırabilirsiniz")
