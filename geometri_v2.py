import math
from turtle import *
def cos(x):
    return round(math.cos(math.radians(x)),6)
def sin(x):
    return round(math.sin(math.radians(x)),6)
def acos(x):
    degerler=[]
    degerler.append(round(math.degrees(math.acos(x)),6))
    degerler.append(360-degerler[0])
    return degerler
def asin(x):
    degerler=[]
    if x>=0:
        degerler.append(round(math.degrees(math.asin(x)),6))
        degerler.append(180-degerler[0])
    else:
        degerler.append(round(180+math.degrees(math.asin(x))-2*math.degrees(math.asin(x)),6))
        degerler.append(360+round(math.degrees(math.asin(x)),6))
    return degerler
acilar=[]
kenarlar=[]
alanlar=[]
kacgen=0
dogru_degerler=True
print("Çıkmak için CTRL+C tuşuna basınız!")
while kacgen<3:
    try:
        kacgen=int(input("\nKaçgen olsun?\t"))
        if kacgen<3:
            print("\nÇokgenler en az 3 kenarlıdır!")
    except ValueError:
        print("\nÇokgenlerin kenar sayısı sadece tam sayı olur!")
    except KeyboardInterrupt:
        print("\nÇıkıldı")
        quit()
toplam_aci=(kacgen-2)*180
deger_turu=-1
while deger_turu<0 or deger_turu>1:
    try:
        deger_turu=int(input("""\nHangi bilinmeyenler olsun?
0:\t1 kenar 2 açı
1:\t2 kenar 1 açı
Birini seç:\t"""))
        if deger_turu<0 or deger_turu>1:
            print("\nSadece 0 veya 1 girin (yukarıda yazıyor!)")
    except ValueError:
        print("\nSadece 0 veya 1 girin (yukarıda yazıyor!)")
if deger_turu==1:
    for i in range(kacgen-2):
        aci=0
        while aci<=0 or aci>=180:
            try:
                aci=180-float(input(f"\n{i+1}. açı kaç derece olsun?\t"))
                if aci<=0 or aci>=180:
                    print("\nİç açılar 0° ile 180° arasında olmalı!")
            except ValueError:
                print("\nSadece reel sayılar giriniz!")
            except KeyboardInterrupt:
                print("\nÇıkıldı")
                quit()
        acilar.append(aci if aci!=int(aci) else int(aci))
        kenar=0
        while kenar<=0:
            try:
                kenar=float(input(f"\n{i+1}. kenar kaç pixel olsun?\t"))
                if kenar<=0:
                    print("\nUzunluklar negatif sayılar olamaz!")
            except ValueError:
                print("\nSadece reel sayılar giriniz!")
            except KeyboardInterrupt:
                print("\nÇıkıldı")
                quit()
        kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
    aci=0
    while (aci<=0 or aci>=180) and dogru_degerler:
        try:
            aci=180-float(input(f"\n{len(acilar)+1}. açı kaç derece olsun?\t"))
            if aci<=0 or aci>=180:
                print("\nİç açılar 0° ile 180° arasında olmalı!")
        except ValueError:
            print("\nSadece reel sayılar giriniz!")
        except KeyboardInterrupt:
            print("\nÇıkıldı")
            quit()
    acilar.append(aci if aci!=int(aci) else int(aci))
    acilar.append(360-sum(acilar))
    kosegen0=kenarlar[0]
    kosegen_aci0=180-acilar[1]
    alanlar=[]
    for i in range(1,kacgen-2):
        alanlar.append(kosegen0*kenarlar[i]*sin(kosegen_aci0)/2)
        kosegen1=(kenarlar[i]**2+kosegen0**2-2*kenarlar[i]*kosegen0*cos(kosegen_aci0))**0.5
        kosegen_aci0=180-acilar[i+1]-acos((kosegen0**2-kenarlar[i]**2-kosegen1**2)/(-2*kosegen1*kenarlar[i]))[0]
        kosegen0=kosegen1
    kosegen_aci1=180-(180-acilar[len(acilar)-1]+kosegen_aci0)
    oran=kosegen0/sin(180-acilar[len(acilar)-1])
    kenar=oran*sin(kosegen_aci1)
    kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
    kenar=oran*sin(kosegen_aci0)
    kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
    alanlar.append(kosegen0*kenarlar[len(kenarlar)-2]*sin(kosegen_aci0)/2)
elif deger_turu==0:
    for i in range(kacgen-2):
        kenar=0
        while kenar<=0:
            try:
                kenar=float(input(f"\n{i+1}. kenar kaç pixel olsun?\t"))
                if kenar<=0:
                    print("\nUzunluklar negatif sayılar olamaz!")
            except ValueError:
                print("\nSadece reel sayılar giriniz!")
            except KeyboardInterrupt:
                print("\nÇıkıldı")
                quit()
        kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
        aci=0
        while aci<=0 or aci>=180:
            try:
                aci=180-float(input(f"\n{i+1}. açı kaç derece olsun?\t"))
                if aci<=0 or aci>=180:
                    print("\nİç açılar 0° ile 180° arasında olmalı!")
            except ValueError:
                print("\nSadece reel sayılar giriniz!")
            except KeyboardInterrupt:
                print("\nÇıkıldı")
                quit()
        acilar.append(aci if aci!=int(aci) else int(aci))
    kenar=0
    while kenar<=0:
        try:
            kenar=float(input(f"\n{len(kenarlar)+1}. kenar kaç pixel olsun?\t"))
            if aci<=0 or aci>=180:
                print("\nSadece reel sayılar giriniz!")
        except ValueError:
            print("\nSadece reel sayılar giriniz!")
        except KeyboardInterrupt:
            print("\nÇıkıldı")
            quit()
    kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
    kosegen0=kenarlar[0]
    kosegen_aci0=180-acilar[0]
    alanlar=[]
    for i in range(1,kacgen-2):
        alanlar.append(kosegen0*kenarlar[i]*sin(kosegen_aci0)/2)
        kosegen1=(kenarlar[i]**2+kosegen0**2-2*kenarlar[i]*kosegen0*cos(kosegen_aci0))**0.5
        kosegen_aci0=180-acilar[i]-acos((kosegen0**2-kenarlar[i]**2-kosegen1**2)/(-2*kosegen1*kenarlar[i]))[0]
        kosegen0=kosegen1
    kenar=(kenarlar[len(kenarlar)-1]**2+kosegen0**2-2*kenarlar[len(kenarlar)-1]*kosegen0*cos(kosegen_aci0))**0.5
    kenarlar.append(kenar if kenar!=int(kenar) else int(kenar))
    aci=180-acos((kosegen0**2-kenarlar[len(kenarlar)-2]**2-kenarlar[len(kenarlar)-1]**2)/(-2*kenarlar[len(kenarlar)-2]*kenarlar[len(kenarlar)-1]))[0]
    acilar.append(aci if aci!=int(aci) else int(aci))
    acilar.append(360-sum(acilar))
    alanlar.append(kenar*kenarlar[len(kenarlar)-2]*sin(180-acilar[len(acilar)-2])/2)
konumlar=[]
title("Geometri")
setup(800,600)
begin_fill()
konumlarX=[]
konumlarY=[]
for i in range(len(kenarlar)):
    konumlar.append(pos())
    fd(kenarlar[i])
    lt(acilar[(i+1)%len(kenarlar)] if deger_turu else acilar[i])
    x=round(list(pos())[0],2) if round(list(pos())[0],2)!=int(round(list(pos())[0],2)) else int(round(list(pos())[0],2))
    y=round(list(pos())[1],2) if round(list(pos())[1],2)!=int(round(list(pos())[1],2)) else int(round(list(pos())[1],2))
    konumlarX.append(x)
    konumlarY.append(y)
    kenar=round(kenarlar[i],2)
    aci=round(180-acilar[(i+1)%kacgen if deger_turu else i],2)
    print(f"\n{i+1}.",f"{kenar if kenar!=int(kenar) else int(kenar)}px",f"{aci if aci!=int(aci) else int(aci)}°",f"x: {x}",f"y: {y}",sep="\t")
end_fill()
cevre=round(sum(kenarlar),2) if round(sum(kenarlar),2)!=int(round(sum(kenarlar),2)) else int(round(sum(kenarlar),2))
alan=round(sum(alanlar),2) if round(sum(alanlar),2)!=int(round(sum(alanlar),2)) else int(round(sum(alanlar),2))
merkezX=round(sum(konumlarX)/len(konumlarX),2) if round(sum(konumlarX)/len(konumlarX),2)!=int(round(sum(konumlarX)/len(konumlarX),2)) else int(round(sum(konumlarX)/len(konumlarX),2))
merkezY=round(sum(konumlarY)/len(konumlarY),2) if round(sum(konumlarY)/len(konumlarY),2)!=int(round(sum(konumlarY)/len(konumlarY),2)) else int(round(sum(konumlarY)/len(konumlarY),2))
print(f"\nÇevre: {cevre}px",f"Alan: {alan}px^2",sep="\t\t")
print(f"\nMerkez Noktası:\t",f"x: {merkezX}",f"y: {merkezY}",sep="\t")
hideturtle()
try:
    input("\nÇıkmak için \"Enter\" tuşuna bas\t")
    exit()
except KeyboardInterrupt:
    exit()
