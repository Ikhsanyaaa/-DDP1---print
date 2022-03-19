#tuple

#membuat tuple
tuple1 = ("apel", "pisang", 3000, 80000)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("a", "b", "c", "d", "e")

#menampilkan tuple
for i in tuple2 :
    print(i)

#mengakses nilai tuple

print("tuple [0] : ", tuple2[0])
print("tuple [1-5] : ", tuple2[0:5])

#mengupdate nilai tuple

buah = ("apel", "mangga", "pisang", "nanas")
print("tuple buah : ",buah)
print("nilai pada indeks 1 : ", buah[1])
buah = list(buah)
buah[1] = "durian"
buah = tuple(buah)
print(buah)
print("nilai pada indeks 1 : ", buah[1])

#menghapus nilai pada tuple
print("tuple sebelum dihapus : ", buah)
buah = list(buah)
del buah[3]
buah = tuple(buah)
print("tuple setelah dihapus : ", buah)

#menambahkan nilai pada tuple

print("tuple sebelum ditambahkan : ", buah)
buah = list(buah)
buah.append ("nangka")
buah = tuple(buah)
print("tuple sesudah ditambahkan : ", buah)
