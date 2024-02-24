

class KasetPlaystation:
    def __init__(self, judul, harga, stok, release, tipe):
        self.judul = judul
        self.harga = harga
        self.stok = stok
        self.release = release
        self.tipe = tipe


class PenjualKasetPlaystation:
    def __init__(self):
        self.daftarKaset = [
            KasetPlaystation("Judul1", 50000, 10, "01-01-2024", "4"),
            KasetPlaystation("Judul2", 55000, 8, "02-01-2024", "5"),
            KasetPlaystation("Judul3", 40000, 15, "03-01-2024", "4"),
        ]

    def tambahKaset(self, judul, harga, stok, release, tipe):
        kasetBaru = KasetPlaystation(judul, harga, stok, release, tipe)
        self.daftarKaset.append(kasetBaru)
        print(f"Kaset {judul} telah ditambahkan.")

    def lihatSemuaKaset(self):
        print("Daftar Kaset PlayStation yang Tersedia:")
        for kaset in self.daftarKaset:
            print(f"Judul: {kaset.judul}, Harga: {kaset.harga}, Stok: {kaset.stok}, tanggal release: {kaset.release}, Playstation: {kaset.tipe}")

    def cariKaset(self, judul):
        for kaset in self.daftarKaset:
            if kaset.judul.lower() == judul.lower():
                return kaset
        return None


    def updateKasetJudul(self,judulBaru):
        kaset = self.cariKaset(judul)
        if kaset:
            kaset.judul = judulBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetHarga(self, hargaBaru):
        kaset = self.cariKaset(judul)
        if kaset:
            kaset.harga = hargaBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetStok(self,stokBaru):
        kaset = self.cariKaset(judul)
        if kaset:
            kaset.stok = stokBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetRelease(self,releaseBaru):
        kaset = self.cariKaset(judul)
        if kaset:
            kaset.release = releaseBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetTipe(self,tipeBaru):
        kaset = self.cariKaset(judul)
        if kaset:
            kaset.tipe = tipeBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")


    def hapusKaset(self, judul):
        kaset = self.cariKaset(judul)
        if kaset:
            self.daftarKaset.remove(kaset)
            print(f"Kaset {judul} telah dihapus dari daftar.")
        else:
            print(f"Kaset {judul} tidak ditemukan dalam daftar.")


admin = PenjualKasetPlaystation()


while True:
    try:
        print("1. Tambah Kaset")
        print("2. Lihat Daftar kaset")
        print("3. Ubah Data Kaset")
        print("4. Hapus Data Kaset")
        print("0. Keluar")
        opsi = input("Masukkan pilihan: ")
        if opsi == "1":
            judul = input("Masukkan Judul Game: ").strip()
            harga = int(input("Masukkan Harga kaset: "))
            stok = int(input("Masukkan Stok Kaset: "))
            release = input("Masukkan tanggal release game: ")
            tipe = input("Kaset PS berapa: ")
            admin.tambahKaset(judul, harga, stok, release, tipe)
            admin.lihatSemuaKaset()
        elif opsi == "2":
            admin.lihatSemuaKaset()
        elif opsi == "3":
            while True:
                admin.lihatSemuaKaset()
                judul = input("Masukkan judul kaset yang ingin diubah: ")
                print("1. Ubah Judul")
                print("2. Ubah Harga")
                print("3. Ubah Stok")
                print("4. Ubah Tanggal Release")
                print("5. Ubah Tipe kaset PS")
                print("0. Tidak Jadi")
                pilih = input("Data yang ingin diubah: ")
                if pilih == "1":
                    judulBaru = input("Masukkan Judul baru: ")
                    admin.updateKasetJudul(judulBaru)
                elif pilih == "2":
                    hargaBaru = int(input("Masukkan Harga baru: "))
                    admin.updateKasetHarga(hargaBaru)
                elif pilih == "3":
                    stokBaru = int(input("Masukkan Stok baru: "))
                    admin.updateKasetStok(stokBaru)
                elif pilih == "4":
                    releaseBaru = input("Masukkan tanggal release: ")
                    admin.updateKasetRelease(releaseBaru)
                elif pilih == "5":
                    tipeBaru = input("Masukkan tipe kaset PS: ")
                    admin.updateKasetTipe(tipeBaru)
                elif pilih =="0":
                    break
        elif opsi == "4":
            judul = input("Masukkan Judul Kaset game yang ingin dihapus: ")
            admin.hapusKaset(judul)
        elif opsi == "0":
            print("Terima Kasih sudah menggunakan Program ini")
            break
    except:
        print("Invalid Value")