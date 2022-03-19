#list

#membuat list
list1 = ["apel", "pisang", 3000, 80000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d", "e"]

#menampilkan list
for i in list2 :
    print(i)

#mengakses nilai list

print("list [0] : ", list[0])
print("list [1-5] : ", list[0:5])

#mengupdate nilai list

buah = ["apel", "mangga", "pisang", "nanas"]
print("list buah : ", buah)
print("nilai pada indeks 1 : ", buah[1])
buah[1] = "durian"
print("nilai pada indeks 1 setelah di update : ", buah[2])
print("list buah setelah di update : ",buah)

#menghapus nilai pada list
print("list sebelum dihapus : ", buah)
del buah[3]
print("list setelah dihapus : ", buah)

#menambahkan nilai pada list

print("list sebelum ditambahkan : ", buah)
buah.append ("nangka")
print("list sesudah ditambahkan : ", buah)


