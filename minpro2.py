from datetime import datetime

class KasetPlaystation:
    def __init__(self, judul, harga, stok, release, tipe):
        self.judul = judul
        self.harga = harga
        self.stok = stok
        self.release = release
        self.tipe = tipe

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class PenjualKasetPlaystation:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambahKaset(self, judul, harga, stok, release, tipe):
        newNode = Node(KasetPlaystation(judul, harga, stok, release, tipe))
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def jumlahNode(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 1
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count

    def tambahAwal(self, judul, harga, stok, release, tipe):
        newNode = Node(KasetPlaystation(judul, harga, stok, release, tipe))
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def tambahAkhir(self, judul, harga, stok, release, tipe):
        newNode = Node(KasetPlaystation(judul, harga, stok, release, tipe))
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def tambahDiantara(self, judul, harga, stok, release, tipe):
        if pos < 1 or pos > self.jumlahNode():
            print("Posisi tidak valid.")
            return

        if pos == 1:
            self.tambahAwal(judul, harga, stok, release, tipe)
            return

        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        newNode = Node(KasetPlaystation(judul, harga, stok, release, tipe))
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp

    def lihatSemuaKaset(self):
        if self.head is None:
            print("Daftar kaset kosong.")
        else:
            temp = self.head
            print("[DAFTAR KASET]")
            while temp is not None:
                print(f"Judul: {temp.data.judul}, Harga: {temp.data.harga}, Stok: {temp.data.stok}, tanggal release: {temp.data.release}, Playstation: {temp.data.tipe}")
                temp = temp.next

    def cariKaset(self, judul):
        temp = self.head
        while temp is not None:
            if temp.data.judul.lower() == judul.lower():
                return temp
            temp = temp.next
        return None

    def updateKasetJudul(self,judulBaru):
        node = self.cariKaset(judul)
        if node is not None:
            node.data.judul = judulBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetHarga(self,hargaBaru):
        node = self.cariKaset(judul)
        if node is not None:
            node.data.harga = hargaBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetStok(self,stokBaru):
        node = self.cariKaset(judul)
        if node is not None:
            node.data.stok = stokBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetRelease(self,releaseBaru):
        node = self.cariKaset(judul)
        if node is not None:
            node.data.release = releaseBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def updateKasetTipe(self,tipeBaru):
        node = self.cariKaset(judul)
        if node is not None:
            node.data.tipe = tipeBaru
            print(f"Informasi kaset {judul} telah diperbarui.")
        else:
            print(f"Kaset {judul} tidak ditemukan.")

    def hapusAwal(self):
        if self.head is None:
            print("Linked list kosong.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            print(f"Kaset {judul} telah dihapus dari daftar.")
        else:
            self.head = self.head.next
            self.head.prev = None
            print(f"Kaset {judul} telah dihapus dari daftar.")

    def hapusAkhir(self):
        if self.head is None:
            print("Linked list kosong.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            print(f"Kaset {judul} telah dihapus dari daftar.")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            print(f"Kaset {judul} telah dihapus dari daftar.")

    def hapusKaset(self, judul):
        node = self.cariKaset(judul)
        if node is not None:
            if node == self.head:
                self.head = node.next
            else:
                node.prev.next = node.next
            if node == self.tail:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
            print(f"Kaset {judul} telah dihapus dari daftar.")
        else:
            print(f"Kaset {judul} tidak ditemukan dalam daftar.")

admin = PenjualKasetPlaystation()

while True:
        print("1. Tambah Kaset")
        print("2. Lihat Daftar kaset")
        print("3. Ubah Data Kaset")
        print("4. Hapus Data Kaset")
        print("0. Keluar")
        opsi = input("Masukkan pilihan: ")
        if opsi == "1":
            print("1. Tambah di awal")
            print("2. Tambah di akhir")
            print("3. Tambah di antara")
            pilih = input("Masukkan pilihan: ")
            if pilih == "1":
                judul = input("Masukkan Judul Game: ").strip()
                harga = int(input("Masukkan Harga kaset: "))
                stok = int(input("Masukkan Stok Kaset: "))
                while True:
                    release = input("Masukkan tanggal Release [format: DD/MM/YYYY]: ")
                    if release.strip():
                        try:
                            datetime.strptime(release, "%d/%m/%Y")
                            break
                        except ValueError:
                            print("> FORMAT TANGGAL TIDAK VALID")
                tipe = input("Kaset PS berapa: ")
                admin.tambahAwal(judul, harga, stok, release, tipe)
                admin.lihatSemuaKaset()
            elif pilih == "2":
                judul = input("Masukkan Judul Game: ").strip()
                harga = int(input("Masukkan Harga kaset: "))
                stok = int(input("Masukkan Stok Kaset: "))
                while True:
                    release = input("Masukkan tanggal Release [format: DD/MM/YYYY]: ")
                    if release.strip():
                        try:
                            datetime.strptime(release, "%d/%m/%Y")
                            break
                        except ValueError:
                            print("> FORMAT TANGGAL TIDAK VALID")
                tipe = input("Kaset PS berapa: ")
                admin.tambahAkhir(judul, harga, stok, release, tipe)
                admin.lihatSemuaKaset()
            elif pilih == "3":
                judul = input("Masukkan Judul Game: ").strip()
                harga = int(input("Masukkan Harga kaset: "))
                stok = int(input("Masukkan Stok Kaset: "))
                while True:
                    release = input("Masukkan tanggal Release [format: DD/MM/YYYY]: ")
                    if release.strip():
                        try:
                            datetime.strptime(release, "%d/%m/%Y")
                            break
                        except ValueError:
                            print("> FORMAT TANGGAL TIDAK VALID")
                tipe = input("Kaset PS berapa: ")
                pos = int(input("Masukkan diposisi: "))
                admin.tambahDiantara(judul, harga, stok, release, tipe)
                admin.lihatSemuaKaset()
        elif opsi == "2":
            admin.lihatSemuaKaset()
        elif opsi == "3":
            while True:
                print("1. Ubah Judul")
                print("2. Ubah Harga")
                print("3. Ubah Stok")
                print("4. Ubah Tanggal Release")
                print("5. Ubah Tipe kaset PS")
                print("0. Keluar")
                pilih = input("Data yang ingin diubah: ")
                if pilih == "1":
                    admin.lihatSemuaKaset()
                    judul = input("Masukkan judul kaset yang ingin diubah: ")
                    judulBaru = input("Masukkan Judul baru: ")
                    admin.updateKasetJudul(judulBaru)
                elif pilih == "2":
                    admin.lihatSemuaKaset()
                    judul = input("Masukkan judul kaset yang ingin diubah: ")
                    hargaBaru = int(input("Masukkan Harga baru: "))
                    admin.updateKasetHarga(hargaBaru)
                elif pilih == "3":
                    admin.lihatSemuaKaset()
                    judul = input("Masukkan judul kaset yang ingin diubah: ")
                    stokBaru = int(input("Masukkan Stok baru: "))
                    admin.updateKasetStok(stokBaru)
                elif pilih == "4":
                    admin.lihatSemuaKaset()
                    judul = input("Masukkan judul kaset yang ingin diubah: ")
                    while True:
                        releaseBaru = input("Masukkan tanggal Release [format: DD/MM/YYYY]: ")
                        if releaseBaru.strip():
                            try:
                                datetime.strptime(releaseBaru, "%d/%m/%Y")
                                break
                            except ValueError:
                                print("> FORMAT TANGGAL TIDAK VALID")
                    admin.updateKasetRelease(releaseBaru)
                elif pilih == "5":
                    admin.lihatSemuaKaset()
                    judul = input("Masukkan judul kaset yang ingin diubah: ")
                    tipeBaru = input("Masukkan tipe kaset PS: ")
                    admin.updateKasetTipe(tipeBaru)
                elif pilih =="0":
                    break
        elif opsi == "4":
            while True:
                print("1. Hapus data awal")
                print("2. Hapus data akhir")
                print("3. Hapus menggunakan nama")
                print("0. Keluar")
                pilih = input("Masukkan pilihan: ")
                if pilih == "1":
                    admin.hapusAwal()
                elif pilih == "2":
                    admin.hapusAkhir()
                elif pilih == "3":
                    judul = ("Masukkan judul yang ingin dihapus: ")
                    admin.hapusKaset()
                elif pilih == "0":
                    break
                else:
                    print("Invalid Value")
        elif opsi == "0":
            print("Terima Kasih sudah menggunakan Program ini")
            break
        else:
            print("Invalid Value")