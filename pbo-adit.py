print()
print("===================================")
print("Program untuk menghitung pajak penghasilan")
print("===================================")
print()

from abc import ABC, abstractmethod 		#mengambil nilai abc dan melakukan import terhadap modul ABC dan abstractmethod

class Storage(ABC):			#class Storage sebagai induk kelas
  @staticmethod
  def simpan():
    file = open(self.get_file(),"")			#digunakan untuk membuka file yang akan dibaca pada get_file
    for key,data in self.get_data():
      data = file.write("%s: %s \n"%(key,data))			#membuka dan menuliskan isi yang terdapat pada get_data

  @abstractmethod
  def get_file(self):				#melakukan akses terhadap function get_file menggunakan abstractmethod
      pass

  @abstractmethod
  def get_data(self):													#melakukan akses terhadap function get_data menggunakan abstractmethod
      pass

class Wajib_Pajak(Storage):					#mendefinisikan class WajibPajak yang merupakan kelas turunan dan mengekstend induk kelas yaitu class Storage
  def __init__(self,nama,pekerjaan,gaji,beban,total):			#mendefinisikan __init__ yang menginisiasi pembuatan objek yang terdiri atas nama,pekerjaan,gaji,beban,total
    self.nama = nama										#memanggil variabel nama menggunakan self karena harus memanggil dirinya sendiri baru methodnya
    self.pekerjaan = pekerjaan			#memanggil variabel pekerjaan menggunakan self karena harus memanggil dirinya sendiri baru methodnya
    self.gaji = gaji			#memanggil gaji nama menggunakan self karena harus memanggil dirinya sendiri baru methodnya
    self.beban = beban							#memanggil beban nama menggunakan self karena harus memanggil dirinya sendiri baru methodnya
    self.file = "pajak.txt"				#memanggil file pajak.txt yang digunakan untuk mengisi data yang akan diinputkan 
  
  def get_data(self):			#mendefinisikan function get_data untuk memanggil variabel yang ada di dalam function
    dictPajak = {
      "nama": self.nama,			#memanggil variabel nama
      "pekerjaan": self.pekerjaan,		#memanggil variabel pekerjaan
      "gaji": self.gaji,				#memanggil variabel gaji
      "beban": self.beban,			#memanggil variabel beban
	  "total": self.total,		#memanggil variabel total
    }
    return dictPajak		#mengembalikan nilai dari dictPajak

  def get_file(self):			#mendefinisikan function get_file
    return self.file			#mengembalikan nilai dari get_file
	
#class Beban_Pajak():
def input_data(nama,pekerjaan,gaji,beban):		#mendefinisikan variabel yang akan diinputkan pada console ada nama,pekerjaan,gaji,beban
	file = open("pajak.txt","a")		#membuka file pajak.txt yang akan menampung hasil inputan pada console, "a" sebagai parameter bahwa bisa dilakukan penambahan data pada file
	data = file.write("nama: %s \n"%(nama))		#menuliskan nama yang akan diinputkan
	data = file.write("pekerjaan: %s \n"%(pekerjaan))		#menuliskan pekerjaan yang akan diinputkan
	data = file.write("gaji: %i \n"%(gaji))		#menuliskan gaji yang akan diinputkan
	data = file.write("beban: %i \n"%(beban))	#melakukan penghitungan beban dengan rumus yang sudah tersedia
	data = file.write("total: %i \n"%(total))	#melakukan penghitungan total dengan rumus yang sudah tersedia
	
def tampilkan_rincian():			#mendefinisikan function tampilkan_rincian
	file = open("pajak.txt","r")		#membuka file pajak.txt setelah dilakukan inputan dan hanya membaca saja
	print(file.read())#melakukan eksekusi pembacaan pada file
	
def option():		#mendefinisikan function untuk melakukan inputan yang sudah terdapat ketentuan tersendiri
	print("Pilihlah Salah Satu dibawah Ini: ")
	print("1. Hitung Pajak Penghasilan")	#memasukkan angka 1 maka operasinya Hitung Pajak Penghasilan
	print("2. Tampilkan Hasil Penghitungan")	#memasukkan angka 2 maka operasinya Tampilkan Hasil Penghitungan
	print("3. Keluar Program")								#memasukkan angka 3 maka operasinya Keluar Program
	pilihan = int(input("Masukan pilihan Anda: "))	#memasukkan angka sebagai inputan untuk melanjutkan eksekusi program(angka 1,2 atau 3), selain itu maka program error
	return pilihan																				#mengembalikan nilai variabel pilihan
	
pilihan = True
while (pilihan<3):	#kondisi jika pilihan kurang dari 3
	pilihan = option()	#variabel pilihan memiliki posisi yang sama atau tergantung dengan function option
	if(pilihan == 1):	#jika memasukkan pilihan 1 maka hasilnya
		nama = str(input("  Nama : "))	#masukkan nama dengan tipe data string
		pekerjaan = str(input("  Pekerjaan : "))	#masukkan nama dengan tipe data pekerjaan
		gaji = int(input("  Masukkan gaji : Rp."))	#masukkan nama dengan tipe data integer
		beban = 2/100 * gaji	#menghitung beban gaji dengan rumus 2% dari gaji yang sudah diinputkan
		print("Beban pajak yang harus dibayarkan per bulan : Rp.",beban)	#menampilkan hasil penghitungan beban
		total = 12 * beban	#menghitung beban gaji dengan rumus 12 dikalikan dengan beban yang sudah diinputkan(dalam ukuran 1 tahun ada 12 bulan)
		print("Total pajak yang dibayarkan dalam setahun : Rp.",total)	#menampilkan hasil penghitungan total
		input_data(nama,pekerjaan,gaji,beban)	#menginputkan data ke dalam file pajak.txt berupa nama,pekerjaan,gaji,beban
	elif(pilihan == 2):	#jika memasukkan pilihan 2 maka 
		tampilkan_rincian()	#menampilkan hasil inputan yang sudah dilakukan pada pilihan 1
	elif (pilihan == 3):	#jika memasukkan angka 3 maka 
		break	#dilakukan penghentian eksekusi atau keluar dari program yang sudah ditampilkan
	print()	#menampilkan perintah yang sudah dieksekusi pada variabel pilihan