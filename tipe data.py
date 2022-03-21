#tipe list, tipe data yang paling serbaguna yang tersedia dalam bahasa python
#yang dapat ditulis sebagai daftar nilai yang dipisahkan dengan koma(item)
#antara tanda kurung siku
nilai =[1,2,"kanda","dinda",True]
print(nilai)
#pengupdate
nilai[0]=2
print(nilai)
#penambahan
nilai.append(45)
print(nilai)
#remove(menghapus)
nilai.remove(45)
print(nilai)

print("---------------------------------------------------------------------------------")

#tipe data tuple dalam python adalah stuktur data yang di gunakan untuk menyimpan
#sekumpulan data, tuple ini bersifat immutable, artinya isi tuple tidak bisa kita
#ubah dan hapus. manun, dapat kita isi dengan berbagai macam nilai dan objek
pusing =(17,30,"tugas","tugaslagi",True)
print(pusing)

print("---------------------------------------------------------------------------------")

#tipe data set adalah tipe data kolektif yang digunakan untuk menyimpan nilai dalam
#satu varibel dengan ketentuan nilai anggotanya yg di simpan harus unik(tidak duplikat) nilai
#anggotanya yang sudah di masukkan tidak di ubah lagi.
salim ={"m","w",2,"m","a","k"}
print(salim)
#menambahkan
salim.add("kaco")
print(salim)
#remove(penghapusan)
salim.remove("kaco")
print(salim)

print("---------------------------------------------------------------------------------")

#dictionary tipe data ini berfungsi untuk menyimpan data dengan pendekatan key value
m ={"nama":"mursalim","umur":20, "jk":"laki-laki"}
for ss in(m, ):
    print(ss)
