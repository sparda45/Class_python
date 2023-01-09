#membuat class mahasiswa
class Mahasiswa:
    nama = None
    asal = None
    
    #membuat fungsi perkenalan
    def perkenalan (self):
        print(f'Perkenalkan saya {self.nama} dari {self.asal}')

#mendefiniskan dyaz sebagai class mahasiswa dan membuat value dari nama dan asal
dyaz = Mahasiswa()
dyaz.nama = "dyaz"
dyaz.asal = "Jakarta"



# panggil fungsi perkenalan
dyaz.perkenalan()
 