# project_UAS
```sh
Nama    : A. Reza Baehaqa Jamroni
Nim     : 312110494
Matkul  : Bahasa Perograman
```
### Struktur package dan model
![Gambar 1](screenshot/1.png)<p>
### penjelasan

1. daftar_nilai.py berisi modul untuk: tambah, ubah, hapus, cari
### tambah
* Fungsi tambah untuk menambahkan data mahasiswa seperti nama, nim, nilai tugas, nilai uts dan nilai uas dengan menggunakan fungsi nama_input(), nim_input(), tugas_input(), uts_input(), uas_input(). Data yang diinput akan masuk ke dalam direktori dt={}
```sh
def tambah(self):
        print('\n\033[95mTambah Data Mahasiswa')
        input_nama  = nama()
        input_nim   = nim()
        input_tugas = tugas()
        input_uts   = uts()
        input_uas   = uas()
        input_akhir = akhir()
        dt[input_nama]=input_nim,input_tugas,input_uts,input_uas,input_akhir
        print("\n\033[93mData Berhasil Di ditambah!\n")
```
### ubah
* Fungsi ubah untuk mengubah data mahasiswa berdasarkan nama, lalu masukkan data yang ingin diubah.
```sh
def ubah(self):
        print('\n\033[95mMengubah Data Mahasiswa')
        input_nama  = nama()                                                         
        if input_nama in dt.keys():                              
            input_nim   = nim()
            input_tugas = tugas()
            input_uts   = uts()
            input_uas   = uas()
            input_akhir = akhir()
            dt[input_nama]=input_nim,input_tugas,input_uts,input_uas,input_akhir                      
            print("\n\033[93mData Berhasil Di Update!\n")
```
### hapus
* Fungsi hapus untuk menghapus data mahasiswa berdasarkan nama
``` sh
    def hapus(self):
        print('\n\033[95mmenghapus data')
        input_nama = nama()                                                        
        if input_nama in dt.keys():
            z=input('\n\033[93mapakah kamu yakin ingin menghapus (y/t) : ')                                                              
            if z == "y":
                del dt[input_nama]                                                                   
                print("\n\033[93mData Telah dihapus!\n")

            if z == "t":
                print('\n\033[93mKembali ke menu utama')

        else:
            print("\033[93mData Mahasiswa Tidak Ada\n")
```
### cari
* Fungsi cari  untuk mencari data mahasiswa berdasarkan nama
```sh
    def cari_data(self):
        ('+---{  MASUKAN NAMA DARI DATA YANG AKAN DI CARI  }--+\n')
        input_nama  = nama()
        view.cari(self)
```
### keluar 
* fungsi keluar untuk keluar dari program dan menampilkan data diri yang saya bikin
```sh
    def keluar(self):
        print('\n\033[97m=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: A. Reza Baehaqa Jamroni\nKelas\t: TI.21.C5\nNIM\t: 312110494")
        print(21*'=')
```
### output program
berikut adalah hasil dari output yang saya bikin
![Gambar 1](screenshot/2.png)<p>
![Gambar 1](screenshot/3.png)<p>
![Gambar 1](screenshot/4.png)<p>

