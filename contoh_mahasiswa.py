class mahasiswa():
	"dasar kelas untuk semua mahasiswa"
	jmlMhs = 0
	def __init__ (self, nama, prodi,nim,jenis):
		self.nama = nama
		self.prodi = prodi
		self.nim = nim
		self.jenis = jenis
		mahasiswa.jmlMhs += 1
	def tampilJml(self):
		print("Total Mahasiswa: ", mahasiswa.jmlMhs)
	def tampilProfil(self):
		print("Nama : ", self.nama)
		print("Prodi : ", self.prodi)
		print("Nim :", self.nim)
		print("Jenis Kelamin :",self.jenis)
		print()

mhs1 = mahasiswa(" "," "," "," ")

name = input("Nama: ")
sp = input("Prodi: ")
sn = input("Nim :")
la = input("Jenis Kelamin :")

#Cek atribut


print(setattr(mhs1,"Nama",name))
print(setattr(mhs1,"Prodi",sp))
print(setattr(mhs1,"Nim",sn))
print(setattr(mhs1,"Jenis_Kelamin",la))

print("b")

print(hasattr(mhs1,"Nama"))
print(hasattr(mhs1,"Prodi"))
print(hasattr(mhs1,"Nim"))
print(hasattr(mhs1,"Jenis_Kelamin"))

print("c")
print(getattr(mhs1,"jenis"))

print("d")
print(delattr(mhs1,"jenis"))
