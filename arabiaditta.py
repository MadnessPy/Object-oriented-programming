print()
print("===================================")
print("Program untuk menghitung pajak penghasilan")#mencetak program untuk menghitung pajak penghasilan
print("===================================")
print()

from abc import ABC, abstractmethod

class Storage(ABC): #asbtraksi
  @staticmethod
  def simpan():
    file = open(self.get_file(),"")
    for key,data in self.get_data():
      data = file.write("%s: %s \n"%(key,data))

  @abstractmethod
  def get_file(self):#mengambil data file
      pass

  @abstractmethod
  def get_data(self):#mengambil data pajak
      pass

class Wajib_Pajak(Storage):#membuat simpan kelas wajib pajak 
  def __init__(self,nama,pekerjaan,gaji,beban,total): #method init 
    self.nama = nama
    self.pekerjaan = pekerjaan
    self.gaji = gaji
    self.beban = beban
    self.file = "pajak.txt" #file txt yang bernama pajak
  
  def get_data(self):
    dictPajak = {
      "nama": self.nama,
      "pekerjaan": self.pekerjaan,
      "gaji": self.gaji,
      "beban": self.beban,
	  "total": self.total,
    }
    return dictPajak
		
  def get_file(self):  # mrngambil nama file
    return self.file
	
#class Beban_Pajak(): #membuat fungsi beban pajak 
def input_data(nama,pekerjaan,gaji,beban):#dengan memasukan data nama pekerjaan,gaji dan beban 
	file = open("pajak.txt","a") #membuka file txt yang bernama pajak dengan append
	data = file.write("nama: %s \n"%(nama))
	data = file.write("pekerjaan: %s \n"%(pekerjaan))#file wrire yang berfungsi untuk menulis file yaitu nama,pekerjaan,gaji,beban,dan total
	data = file.write("gaji: %i \n"%(gaji))
	data = file.write("beban: %i \n"%(beban))
	data = file.write("total: %i \n"%(total))
	
def tampilkan_rincian(): #akan menapilkan rincian
	file = open("pajak.txt","r")#membuka file  bernama pajak txt 
	print(file.read()) #membaca file
	
def option(): #akan menampilkan fungsi pilihan
	print("Pilihlah Salah Satu dibawah Ini: ") #tampilan untuk memilih hitung pajak penghasilan,tampilkan hasil perhitungan dan keluar program
	print("1. Hitung Pajak Penghasilan")
	print("2. Tampilkan Hasil Penghitungan")
	print("3. Keluar Program")
	pilihan = int(input("Masukan pilihan Anda: "))#memasukan pilihan dengan tipe data yaitu  angka/ integer
	return pilihan 
	
pilihan = True
while (pilihan<3):
	pilihan = option()
	if(pilihan == 1):
		nama = str(input("  Nama : ")) #memasukan nama,pekerjaan dan masukkan gaji dengan tipe data string
		pekerjaan = str(input("  Pekerjaan : "))
		gaji = int(input("  Masukkan gaji : Rp."))
		beban = 2/100 * gaji
		print("Beban pajak yang harus dibayarkan per bulan : Rp.",beban)
		total = 12 * beban
		print("Total pajak yang dibayarkan dalam setahun : Rp.",total)
		input_data(nama,pekerjaan,gaji,beban)
	elif(pilihan == 2):
		tampilkan_rincian()
	elif (pilihan == 3): 
		break
