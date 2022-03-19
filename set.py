#set

#membuat set
set1 = {"apel", "pisang", 3000, 80000}
set2 = {1, 2, 3, 4, 5}
set3 = {"a", "b", "c", "d", "e"}

#menampilkan set
for i in set2 :
    print(i)

#mengakses nilai set
#set bersifat unoredered atau tidak berurut sehingga tidak bisa dipanggil dengan indeks

#mengupdate nilai set
#set bersifat unchangable, yang berarti bahwa nilai yang dimasukkan dalam set, tidak bisa diganti lagi
#akan tetapi kita tetap bisa menambah dan menghapus anggota pada set    

#menghapus nilai pada set
buah = {"apel", "mangga", "pisang", "nanas"}
print("set sebelum dihapus : ", buah)
buah.remove("nanas")
print("set setelah dihapus : ", buah)

#menambahkan nilai pada set

print("set sebelum ditambahkan : ", buah)
buah.add ("durian")
print("set sesudah ditambahkan : ", buah)
