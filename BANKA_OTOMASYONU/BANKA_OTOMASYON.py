
import random

kullanicilar = []

#görevli menü fonksiyonları
def kullanici_ekle():
    try:

        kullanici_numarasi = random.randint(10000, 100000)
        musteri_ilk_sifre = random.randint(1000, 10000)
        yeni_kullanici = {
            'kullanici_numarasi': kullanici_numarasi,
            'isim': input("İsmini girin: "),
            'soyisim': input("Soyismini girin: "),
            'tc': input("Müşterinin TC kimlik numarası: "),
            'telefon_numarasi': input("Müşterinin telefon numarası: "),
            'musteri_ilk_sifre': musteri_ilk_sifre,
            'ilk_sifre_durum': 0,
            'musteri_sifre': 0,
            'bakiye': 0,
            't_cashback': 0
        }
        kullanicilar.append(yeni_kullanici)
        kullanici_bilgisi = f"kUL.NUM:{kullanici_numarasi},|İSİM:{yeni_kullanici['isim']},|SOYİSİM:{yeni_kullanici['soyisim']}," \
                            f"|TC:{yeni_kullanici['tc']},|TELNO:{yeni_kullanici['telefon_numarasi']}," \
                            f"|Ş.DURUM:{yeni_kullanici['ilk_sifre_durum']},|İLKŞİFRE:{musteri_ilk_sifre}," \
                            f"|GÜNCELŞİFRE:{yeni_kullanici['musteri_sifre']},|BAKİYE:{yeni_kullanici['bakiye']}," \
                            f"|T.CASHBACK:{yeni_kullanici['t_cashback']}\n"
        tel_bilgi_islem = f"{kullanici_numarasi} kullanıcı numaralı müşterimiz bankamıza hoşgeldiniz.\n" \
                          f"{yeni_kullanici['telefon_numarasi']} nolu telofana gönderdiğimiz tek kullanımlık " \
                          f"İLKŞİFRE:{musteri_ilk_sifre}  'dur .İlk şifrenizi girdikten sonra yeni 4 haneli şifrenizi belirleyiniz.\n\n"

        # kullanıcı bilgilerini kayıt eder
        with open("kullanici_bilgileri.txt", "a", encoding="utf-8") as dosya:
            dosya.write(kullanici_bilgisi)

        # buradakini yeni kayıt olmuş kullanıcıların(müşterilerin) telefonlarına giden İLKŞİFRE mesajların listesi gibi düşünün
        with open("telefon_mesaj.txt", "a", encoding="utf-8") as dosyaa:
            dosyaa.write(tel_bilgi_islem)

        print("Kullanıcı kaydedildi.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
def kullanici_sil():
    try:
        tc = input("Silmek istediğiniz kullanıcının TC kimlik numarasını girin: ")
        kullanici = kullanici_ara(tc)
        if kullanici:
            kullanicilar.remove(kullanici)
            guncel_kullanicilar = [f"kUL.NUM:{k['kullanici_numarasi']},|İSİM:{k['isim']},|SOYİSİM:{k['soyisim']}," \
                                   f"|TC:{k['tc']},|TELNO:{k['telefon_numarasi']}," \
                                   f"|Ş.DURUM:{k['ilk_sifre_durum']},|İLKŞİFRE:{k['musteri_ilk_sifre']}," \
                                   f"|GÜNCELŞİFRE:{k['musteri_sifre']}" \
                                   f"|BAKİYE:{k['bakiye']},|T.CASHBACK:{k['t_cashback']}\n" for k in kullanicilar]

            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(guncel_kullanicilar)

            print("Kullanıcı silindi.")
        else:
            print("Böyle bir kullanıcı bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
def kullanici_listele():

    if kullanicilar:
        for kullanici in kullanicilar:
            print(f"kUL.NUM:{kullanici['kullanici_numarasi']}  |İSİM:{kullanici['isim']}  |SOYİSİM:{kullanici['soyisim']}  "
                  f"|TC:{kullanici['tc']}  |TELNO:{kullanici['telefon_numarasi']}  |Ş.DURUM:{kullanici['ilk_sifre_durum']}  "
                  f"|İLKŞİFRE:{kullanici['musteri_ilk_sifre']} |BAKİYE:{kullanici['bakiye']} |T.CASHBACK:{kullanici['t_cashback']}", sep=' \t')
    else:
        print("Kayıtlı kullanıcı yok.")
def kullanici_guncelle():
    try:
        tc = input("Güncellemek istediğiniz kullanıcının TC kimlik numarasını girin: ")
        kullanici = kullanici_ara(tc)
        if kullanici:
            x = input("İsimi değiştirmek istermisin E/H").upper()
            if x == 'E':
                kullanici['isim'] = input("Yeni isim: ")

            x = input("Soyisimi değiştirmek istermisin E/H").upper()
            if x == 'E':
                kullanici['soyisim'] = input("Yeni soyisim: ")

            x = input("Telefon numarasını değiştirmek istermisin E/H").upper()
            if x == 'E':
                kullanici['telefon_numarasi'] = input("Yeni telefon numarası: ")

            guncel_kullanicilar = [f"kUL.NUM:{k['kullanici_numarasi']},|İSİM:{k['isim']},|SOYİSİM:{k['soyisim']}," \
                                   f"|TC:{k['tc']},|TELNO:{k['telefon_numarasi']}," \
                                   f"|Ş.DURUM:{k['ilk_sifre_durum']},|İLKŞİFRE:{k['musteri_ilk_sifre']}," \
                                   f"|GÜNCELŞİFRE:{k['musteri_sifre']},|BAKİYE:{k['bakiye']},|T.CASHBACK:{k['t_cashback']}\n"
                                   for k in kullanicilar]

            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(guncel_kullanicilar)

            print("Kullanıcı bilgileri güncellendi.")
        else:
            print("Kullanıcı bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
def kampanya_bilgilendirme():
    #sadece bilgilendirme amaçlıdır
    print("Havale ücreti gönderilen miktarın yalnızca %1 'i dir.")
    print("Havale edilen miktar 1000 tl  ve üstü ise komisyon alınmayacak")
    print("Havale edilen miktar 5000 tl  ve üstü ise komisyon alınmayacak ve "
          "%5 cashback yapılacak")
    print("Havale edilen miktar 10000 tl ve üstü ise komisyon alınmayacak ve "
          "%10 cashback yapılacak")
def kullanici_ara(tc):
    for kullanici in kullanicilar:
        if kullanici['tc'] == tc:
            return kullanici
    return None

def kullanici_yukle():
    #önceden kayıtlı olan kullanıcıların bilgilerini sisteme yükler
    # Dosya açma işlemi with open ifadesiyle gerçekleştirildi ve FileNotFoundError hatası durumunda bir hata mesajı yazdırılıyor.
    try:
        with open("kullanici_bilgileri.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya.readlines():
                kullanici = satir.split(',')
                kullanici_numarasi = int(kullanici[0].split(':')[1])
                isim = kullanici[1].split(':')[1]
                soyisim = kullanici[2].split(':')[1]
                tc = kullanici[3].split(':')[1]
                telefon_numarasi = kullanici[4].split(':')[1]
                ilk_sifre_durum = int(kullanici[5].split(':')[1])
                musteri_ilk_sifre = int(kullanici[6].split(':')[1])
                musteri_sifre = (kullanici[7].split(':')[1])
                bakiye = float(kullanici[8].split(':')[1])
                t_cashback = float(kullanici[9].split(':')[1])


                yeni_kullanici = {
                    'kullanici_numarasi': kullanici_numarasi,
                    'isim': isim,
                    'soyisim': soyisim,
                    'tc': tc,
                    'telefon_numarasi': telefon_numarasi,
                    'ilk_sifre_durum': ilk_sifre_durum,
                    'musteri_ilk_sifre': musteri_ilk_sifre,
                    'musteri_sifre': musteri_sifre,
                    'bakiye': bakiye,
                    't_cashback': t_cashback

                }
                kullanicilar.append(yeni_kullanici)
    except Exception as e:
        print("Bir hata oluştu:", str(e))


#kullanıcı menü fonksiyonları
def havale(kullanici, alici_kullanici):
    # iç içe fonksiyon kullanımı
    try:
        print("Havale ücreti gönderilen miktarın %1 'i dir.")
        miktar = float(input("Havale etmek istediğiniz miktarı girin: "))
        komisyon_ucreti = miktar*1/100

        def kampanya_uygulama():
            if miktar >=10000:
                # 10000 tl nin üstünde olduğu için komisyon ücreti alınmadı ve %5 cashback.
                cashback = miktar * 10 / 100
                kullanici['t_cashback'] += cashback
                kullanici['bakiye'] -= (miktar - cashback)
                alici_kullanici['bakiye'] += miktar
                print(" Güncel Bakiyeniz:{}".format(kullanici['bakiye']))

            elif miktar >=5000:
                # 5000 tl nin üstünde olduğu için komisyon ücreti alınmadı ve %5 cashback.
                cashback = miktar*5/100
                kullanici['t_cashback'] += cashback
                kullanici['bakiye'] -= (miktar - cashback)
                alici_kullanici['bakiye'] += miktar
                print(" Güncel Bakiyeniz:{}".format(kullanici['bakiye']))

            elif miktar >= 1000:
                # 1000 tl nin üstünde olduğu için komisyon ücreti alınmadı.
                kullanici['bakiye'] -= miktar
                alici_kullanici['bakiye'] += miktar
                print(" Güncel Bakiyeniz:{}".format(kullanici['bakiye']))
            else:
                #1000 tl nin altında olduğu için komisyon ücreti alındı.
                kullanici['bakiye'] -= (miktar + komisyon_ucreti)
                alici_kullanici['bakiye'] += miktar
                print(" Güncel Bakiyeniz:{}".format(kullanici['bakiye']))

        if miktar <= 0:
            print("Geçersiz miktar! İşlem gerçekleştirilemedi.")
        elif miktar > kullanici['bakiye']:
            print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")
        else:
            kampanya_uygulama()


            # Kullanıcı bilgilerini güncelle
            for i in range(len(kullanicilar)):
                if kullanicilar[i]['kullanici_numarasi'] == kullanici['kullanici_numarasi']:
                    kullanicilar[i] = kullanici
                    break

            # Kullanıcı bilgilerini dosyaya yaz
            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                for kullanici in kullanicilar:
                    dosya.write(f"kUL.NUM:{kullanici['kullanici_numarasi']},|İSİM:{kullanici['isim']},"
                                f"|SOYİSİM:{kullanici['soyisim']},|TC:{kullanici['tc']},"
                                f"|TELNO:{kullanici['telefon_numarasi']},"
                                f"|Ş.DURUM:{kullanici['ilk_sifre_durum']},"
                                f"|İLKŞİFRE:{kullanici['musteri_ilk_sifre']},"
                                f"|GÜNCELŞİFRE:{kullanici['musteri_sifre']},"
                                f"|BAKİYE:{kullanici['bakiye']},|T.CASHBACK:{kullanici['t_cashback']}\n")


            print("Para havale işlemi başarılı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
def paracek(kullanici):
    try:
        miktar = float(input("Çekmek istediğiniz miktarı girin: "))

        if miktar > kullanici['bakiye']:
            print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")
        else:
            kullanici['bakiye'] -= miktar
            print("İşlem başarıyla tamamlandı.")
            print("Güncel bakiyeniz:", kullanici['bakiye'])
            print("Para yatırma işlemi başarılı.")

            # Kullanıcı bilgilerini güncelle
            for i in range(len(kullanicilar)):
                if kullanicilar[i]['kullanici_numarasi'] == kullanici['kullanici_numarasi']:
                    kullanicilar[i] = kullanici
                    break

            # Kullanıcı bilgilerini dosyaya yaz
            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                for kullanici in kullanicilar:
                    dosya.write(f"kUL.NUM:{kullanici['kullanici_numarasi']},|İSİM:{kullanici['isim']},"
                                f"|SOYİSİM:{kullanici['soyisim']},|TC:{kullanici['tc']},"
                                f"|TELNO:{kullanici['telefon_numarasi']},"
                                f"|Ş.DURUM:{kullanici['ilk_sifre_durum']},"
                                f"|İLKŞİFRE:{kullanici['musteri_ilk_sifre']},"
                                f"|GÜNCELŞİFRE:{kullanici['musteri_sifre']},"
                                f"|BAKİYE:{kullanici['bakiye']},|T.CASHBACK:{kullanici['t_cashback']}\n")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
def parayatir(kullanici):
    try:
        print("Güncel bakiyeniz:", kullanici['bakiye'])
        miktar = float(input("Yatırmak istediğiniz miktarı girin: "))

        if miktar <= 0:
            print("Geçersiz miktar! İşlem gerçekleştirilemedi.")
        else:
            kullanici['bakiye'] += miktar
            print("İşlem başarıyla tamamlandı.")
            print("Güncel bakiyeniz:", kullanici['bakiye'])

            # Kullanıcı bilgilerini güncelle
            for i in range(len(kullanicilar)):
                if kullanicilar[i]['kullanici_numarasi'] == kullanici['kullanici_numarasi']:
                    kullanicilar[i] = kullanici
                    break

            # Kullanıcı bilgilerini dosyaya yaz
            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                for kullanici in kullanicilar:
                    dosya.write(f"kUL.NUM:{kullanici['kullanici_numarasi']},|İSİM:{kullanici['isim']},"
                                f"|SOYİSİM:{kullanici['soyisim']},|TC:{kullanici['tc']},"
                                f"|TELNO:{kullanici['telefon_numarasi']},"
                                f"|Ş.DURUM:{kullanici['ilk_sifre_durum']},"
                                f"|İLKŞİFRE:{kullanici['musteri_ilk_sifre']},"
                                f"|GÜNCELŞİFRE:{kullanici['musteri_sifre']},"
                                f"|BAKİYE:{kullanici['bakiye']},|T.CASHBACK:{kullanici['t_cashback']}\n")

            print("Güncel bakiyeniz:", kullanici['bakiye'])
            print("Para yatırma işlemi başarılı.")

            # Kullanıcı bilgilerini güncelle
            for i in range(len(kullanicilar)):
                if kullanicilar[i]['kullanici_numarasi'] == kullanici['kullanici_numarasi']:
                    kullanicilar[i] = kullanici
                    break

            # Kullanıcı bilgilerini dosyaya yaz
            with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
                for kullanici in kullanicilar:
                    dosya.write(f"kUL.NUM:{kullanici['kullanici_numarasi']},|İSİM:{kullanici['isim']},"
                                f"|SOYİSİM:{kullanici['soyisim']},|TC:{kullanici['tc']},"
                                f"|TELNO:{kullanici['telefon_numarasi']},"
                                f"|Ş.DURUM:{kullanici['ilk_sifre_durum']},"
                                f"|İLKŞİFRE:{kullanici['musteri_ilk_sifre']},"
                                f"|GÜNCELŞİFRE:{kullanici['musteri_sifre']},"
                                f"|BAKİYE:{kullanici['bakiye']},|T.CASHBACK:{kullanici['t_cashback']}\n")


    except Exception as e:
        print("Bir hata oluştu:", str(e))
def hesapbilgileri(kullanici):
    print("Hesap Bilgileri:")
    print("KULNUM:", kullanici['kullanici_numarasi'], "|İSİM:", kullanici['isim'], "|SOYİSİM:", kullanici['soyisim'],
          "|TC:", kullanici['tc'], "|TELNO:", kullanici['telefon_numarasi'], "|BAKİYE:", kullanici['bakiye'],
          "|T.CASHBACK:", kullanici['t_cashback'])

#menüler
def ana_menu():

    kullanici_yukle()
    while True:
        # Ana menü
        print("------------------------------------------------------- -")
        print("1 - GÖREVLİ GİRİŞİ")
        print("2 - MÜŞTERİ GİRİŞİ")
        print("3 - ÇIKIŞ")
        secim = int(input("Yapmak istediğiniz işlemin rakamını girin: "))

        if secim == 1:
            gorevli_menu()
        elif secim == 2:
            kullanici_menu()
        elif secim == 3:
            print("Programdan çıkılıyor.")
            quit()
        else:
            print("Hatalı tuşlama. Lütfen tekrar deneyin.")
def gorevli_menu():
    #şifre eklenecek
    while True:
            print("---------------------------------------------------------------------")
            print("1 - KULLANICI EKLE")
            print("2 - KULLANICI SİL")
            print("3 - KULLANICI BİLGİLERİNİ LİSTELE")
            print("4 - KULLANICI ARA")
            print("5 - KULLANICI BİLGİLERİNİ GÜNCELLE")
            print("6 - ÇIKIŞ")
            secim_gorevli_menu = int(input("Yapmak istediğiniz işlemin rakamını girin: "))

            if secim_gorevli_menu == 1:
                kullanici_ekle()
            elif secim_gorevli_menu == 2:
                kullanici_sil()
            elif secim_gorevli_menu == 3:
                kullanici_listele()
            elif secim_gorevli_menu == 4:
                tc = input("Aranacak kullanıcının TC kimlik numarasını girin: ")
                kullanici = kullanici_ara(tc)
                if kullanici:
                    print("Kullanıcı bulundu.")
                    print("KULNUM:", kullanici['kullanici_numarasi'], "|İSİM:", kullanici['isim'],
                          "|SOYİSİM:", kullanici['soyisim'], "|TC:", kullanici['tc'],
                          "|TELNO:", kullanici['telefon_numarasi'], "|Bakiye:", kullanici['bakiye'])
                else:
                    print("Kullanıcı bulunamadı.")

            elif secim_gorevli_menu == 5:
                kullanici_guncelle()
            elif secim_gorevli_menu == 6:
                print("Ana menüye dönülüyor.")
                return
            else:
                print("Hatalı tuşlama. Lütfen tekrar deneyin.")
def kullanici_menu():
    tc = input("Girmek istediğiniz TC kimlik numarasını girin: ")
    kullanici = kullanici_ara(tc)
    if kullanici:
        while True:
                if kullanici['ilk_sifre_durum'] != 0:
                    musteri_sifre = input("Şifrenizi girin: ")
                    if musteri_sifre == kullanici['musteri_sifre']:
                        while True:
                            print("----------------------------------------------")
                            print("Bakiyeniz:{}".format(kullanici['bakiye']))
                            print("1 - PARA ÇEK")
                            print("2 - PARA YATIR")
                            print("3 - PARAYI BAŞKA BİR HESABA HAVALE ET")
                            print("4 - ŞİFRE DEĞİŞTİR")
                            print("5 - KAMPANYALARIM")
                            print("6 - HESAP BİLGİLERİM")
                            print("7 - ÇIKIŞ")
                            secim_musteri_menu = int(input("Yapmak istediğiniz işlemin rakamını girin: "))

                            if secim_musteri_menu == 1:
                                # Para çekme işlemleri
                                paracek(kullanici)
                            elif secim_musteri_menu == 2:
                                # Para yatırma işlemleri
                                parayatir(kullanici)
                            elif secim_musteri_menu == 3:
                                # Havale işlemleri
                                kullanici_tc = input("Havale yapmak istediğiniz kullanıcının TC sini girin: ")
                                alici = kullanici_ara(kullanici_tc)
                                if alici:
                                    havale(kullanici, alici)
                                else:
                                    print("Havale yapılacak kullanıcı bulunamadı.")
                            elif secim_musteri_menu == 4:
                                # Şifre değiştirme
                                while True:
                                    try:
                                        musteri_sifre = input("Lütfen yeni şifre belirleyiniz: ")
                                        musteri_sifre = int(musteri_sifre)
                                        if len(str(musteri_sifre)) == 4:
                                            kullanici['musteri_sifre'] = musteri_sifre
                                            print("Şifre değiştirildi.")
                                            continue
                                        else:
                                            print("Hatalı giriş. Şifre 4 haneli olmalıdır.")
                                    except ValueError:
                                        print("Hatalı giriş. Şifre sadece rakamlardan oluşmalıdır.")
                            elif secim_musteri_menu == 5:
                                # Kampanyalar
                                kampanya_bilgilendirme()
                            elif secim_musteri_menu == 6:
                                # Hesap bilgileri
                                hesapbilgileri(kullanici)
                            elif secim_musteri_menu == 7:
                                print("Ana menüye dönülüyor.")
                                break
                            else:
                                print("Hatalı tuşlama. Lütfen tekrar deneyin.")
                    else:
                        print("Şifre yanlış.")
                else:
                    musteri_sifre = input("Telefonunuza gelen 4 haneli ilk şifrenizi giriniz: ")
                    if musteri_sifre == str(kullanici['musteri_ilk_sifre']):
                        while True:
                            try:
                                musteri_sifre = input("Lütfen 4 haneli yeni şifre belirleyiniz: ")
                                musteri_sifre = int(musteri_sifre)
                                if len(str(musteri_sifre)) == 4:
                                    kullanici['musteri_sifre'] = musteri_sifre
                                    kullanici['ilk_sifre_durum'] = 1
                                    print("Şifre oluşturuldu.")
                                    break
                                else:
                                    print("Hatalı giriş. Şifre 4 haneli olmalıdır.")
                            except ValueError:
                                print("Hatalı giriş. Şifre sadece rakamlardan oluşmalıdır.")
                    else:
                        print("Şifre yanlış.")

    else:
       print("Kullanıcı bulunamadı.")



ana_menu()