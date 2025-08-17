import tkinter as tk
import sıfre_olusturucu as so

pencere = tk.Tk()
pencere.title("şifre oluşturucu")
pencere.geometry("800x600")
pencere.configure(bg="#424242")

şifre_yazı = tk.Label(pencere,text="",bg="#424242",fg="white",font=("Arial",50))
şifre_yazı.place(x=200, y=150)

def şifre_oluşturucu():
    sifre = so.şifre_oluşturma()
    şifre_yazı.configure(text=sifre)

def kopyalama():
    pencere.clipboard_clear()
    pencere.clipboard_append(so.şifre_oluşturma())

şifre_oluşturucu = tk.Button(pencere, text="şifre oluştur", command=şifre_oluşturucu,bg="#30fc85")
şifre_oluşturucu.place(x=300, y=300, width=200, height=120)

kopyalıyıcı = tk.Button(pencere,text="şifreyi panoya kaydet",command=kopyalama)
kopyalıyıcı.place(x=300,y=440,width=200,height=80)

pencere.mainloop()
