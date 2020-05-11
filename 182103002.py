class DataPegawai(object):
	def __init__(self, nama=None, gaji_pokok=None, jabatan=None, alamat=None):
		self.nama = nama
		self.gaji_pokok = gaji_pokok
		self.jabatan = jabatan
		self.alamat = alamat

listPegawai = []
try:
	for i in range(1):
		print("==============DataPegawai==================")
		nama = input("Nama :")
		gaji = int(input("gaji_pokok :"))
		jabatan = input("jabatan :")
		alamat = input("alamat :")
		listPegawai.append(DataPegawai(nama, gaji, jabatan, alamat))
		print()
		print("-------------------------------------------")
		print()

except ValueError:
	print(" masukkan angka saja!!! ")

print("=======DATA PEGAWAI======:\n")

for Pegawai in listPegawai:
	print("Nama:",Pegawai.nama)
	print("gaji:",Pegawai.gaji_pokok)
	print("jabatan:",Pegawai.jabatan)
	print("alamat:",Pegawai.alamat)
	print()
	print("-------------------------------------------")

def panggilpegawai(pegawai):
	assert(pegawai.jabatan == "manajer") 
	return print(" data pegawai tidak dapat di panggil!!! sebagai anggota perusahaan ")

try:
	panggilpegawai(listPegawai[0])
except AssertionError as error:
	print(error)
	print(' jabatan tidak sesuai')
else:
	peg = listPegawai[0].jabatan
	print("jabatan pegawai tidak sesuai ", peg+'1')


