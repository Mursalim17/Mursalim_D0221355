#Assalamu'alaikum warahmatullahi wabarakatuh. perkenalkan nama saya "Mursalim" dengan Nim D0221355.
#sebelumnya mohon maaf divideo codingan kali ini saya tidak memiliki suara di karenakan microfon
#dari laptop saya sedang bermasalah setelah di pake teman saya...
#nah video kali ini kita akan membuat codingan mengenai list untuk menampung barang, menambahkan barang,
#menghapus barang, program dapat mengedit barang
#program dapat menampilkan semua barang, mengetahui apakah barang sudah ada dalam list atau belum,
#dan yang terakhir program dapat menampilkan index barang tertentu
#langsung saja kita masuk pada contoh kodingannya
list=[]
barang = int(input(" masukkan nilai anda : "))
for s in range (barang) :
    barang = str(input(" masukkan nama barang anda : "))
    list.append(barang)
print(list)
  
