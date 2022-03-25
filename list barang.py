Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> barang = []
def menambah() :
    while True :
        barang_baru = str(input("masukkan barang yang ingin dimasukkan ke keranjang : "))
        barang.append(barang_baru)
        done = str(input("apakah masih ada barang yang ingin ditambahkan? (y/t) : "))
        if done == "t" :
            menu()
            break
        elif done != "y" and done != "t" :
            print("masukkan pilihan dengan benar!")
            menu()

def menghapus():
    while True : 
        barang_usang = str(input("masukkan barang yang ingin dihapus : "))
        barang.remove(barang_usang)
        done = str(input("apakah masih ada barang yang ingin dihapus? (y/t) : "))
        if done == "t" :
            print("barang sukses dihapus")
            menu()
            break
        if done != "y" and done != "t" :
            print("masukkan pilihan dengan benar!")

def mengedit():
    cari = str(input("masukkan nama barang yang ingin diganti : "))
    ketemu = False
    for i in range(0, len(barang)) :   
        if cari == barang[i] :
            ketemu = True  
            if ketemu == True :      
                ganti = str(input("masukkan barang baru : "))
                barang[barang.index(cari)] = ganti
                print("barang sukses diganti")
                menu()
            else : 
                print("barang yang dimasukkan tidak sesuai dengan yang ada di list barang!")
                mengedit()
def mencari () : 
    cari = str(input("masukkan nama barang yang ingin dicari : "))
    ketemu = False
    for i in range(0, len(barang)) :    
        if cari == barang[i] :
            ketemu = True        
    if ketemu : 
        print(cari, "ditemukan pada indeks ke : ", barang.index(cari))
        menu()
    else :
        print("barang", cari, "tidak ditemukan!")
        menu()
        
        
def tampilkan():       
    print("barang yang anda telah masukkan ke keranjang adalah :")
    for i in barang :
        print(i)

def menu():
    print("=" * 25)
    tampilkan()
    print('''
    1. menambahkan barang
    2. mengganti barang yang telah dipilih
    3. menghapus barang yang telah dipilih
    4. mencari barang yang telah dipilih''')
    pilihan = int(input("selamat datang di toko serbaguna, silahkan pilih menu diatas! : "))
    if pilihan == 1 :
        menambah()
    elif pilihan == 2 :
        mengedit()
    elif pilihan == 3 :
        menghapus()
    elif pilihan == 4 :
        mencari()

menu()



