print()
print("===================================")
print("Program untuk menghitung pajak penghasilan")
print("===================================")
print()

from abc import ABC, abstractmethod

class Storage(ABC):
  @staticmethod
  def simpan():
    file = open(self.get_file(),"")
    for key,data in self.get_data():
      data = file.write("%s: %s \n"%(key,data))

  @abstractmethod
  def get_file(self):
      pass

  @abstractmethod
  def get_data(self):
      pass

class Wajib_Pajak(Storage):
  def __init__(self,nama,pekerjaan,gaji,beban,total):
    self.nama = nama
    self.pekerjaan = pekerjaan
    self.gaji = gaji
    self.beban = beban
    self.file = "pajak.txt"
  
  def get_data(self):
    dictPajak = {
      "nama": self.nama,
      "pekerjaan": self.pekerjaan,
      "gaji": self.gaji,
      "beban": self.beban,
	  "total": self.total,
    }
    return dictPajak

  def get_file(self):
    return self.file
	
#class Beban_Pajak():
def input_data(nama,pekerjaan,gaji,beban):
	file = open("pajak.txt","a")
	data = file.write("nama: %s \n"%(nama))
	data = file.write("pekerjaan: %s \n"%(pekerjaan))
	data = file.write("gaji: %i \n"%(gaji))
	data = file.write("beban: %i \n"%(beban))
	data = file.write("total: %i \n"%(total))
	
def tampilkan_rincian():
	file = open("pajak.txt","r")
	print(file.read())
	
def option():
	print("Pilihlah Salah Satu dibawah Ini: ")
	print("1. Hitung Pajak Penghasilan")
	print("2. Tampilkan Hasil Penghitungan")
	print("3. Keluar Program")
	pilihan = int(input("Masukan pilihan Anda: "))
	return pilihan
	
pilihan = True
while (pilihan<3):
	pilihan = option()
	if(pilihan == 1):
		nama = str(input("  Nama : "))
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
	print()