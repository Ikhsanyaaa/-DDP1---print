#dictionary

#membuat dictionary
buah = {"nama buah" : "apel", "jumlah" : "3 buah", "harga" : 10000}

#menampilkan dictionary
for i in buah :
    print(i, ":", buah[i])

#mengakses nilai dictionary

print("nama buah : ", buah["nama buah"])
print("jumlah : ", buah["jumlah"])
print("harga : ", buah["harga"])


#mengupdate nilai dictionary

print("nilai pada key jumlah sebelum di update : ", buah["jumlah"])
buah["jumlah"] = "5 buah"
print("nilai pada key jumlah setelah di update : ", buah["jumlah"])

#menghapus nilai pada dictionary

print("dictionary buah sebelum dihapus : ")
for i in buah :
    print(i, ":", buah[i])
del buah["jumlah"]
print("dictionary buah setelah dihapus : ")
for i in buah :
    print(i, ":", buah[i])

#menambahkan nilai pada dictionary

print("dictionary buah sebelum ditambahkan : ")
for i in buah :
    print(i, ":", buah[i])
buah["diskon"] = "20%"
print("dictionary buah setelah ditambahkan : ")
for i in buah :
    print(i, ":", buah[i])



