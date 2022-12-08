class Biodata:
    empCount = 0
    def __init__(self, name, nim, batchyear):
        self.name = name
        self.nim = nim
        self.batchyear = batchyear
        Biodata.empCount += 1
        
    def displayCount(self):
        print("Total Mahasiswa %d" % Biodata.empCount)

    def displayStudent(self):
        print("Nama: ", self.name)
        print("NIM: ", self.nim)
        print("Tahun Angkatan: ", self.batchyear)

name = input("Masukkan Nama anda: ")
nim = int(input("Masukkan NIM anda: "))
batchyear = int(input("Masukkan Tahun Angkatan anda: "))    
    
studentData = Biodata(name, nim, batchyear)
studentData.displayStudent()
print()
print("Total Mahasiswa %d" % Biodata.empCount)