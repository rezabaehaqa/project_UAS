import os
from view.input_nilai import *
import time

dt={}
class daftarNilai():
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

        else:                                                                                    
            print("\n\033[93mData tidak ditemukan!\n")

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
    def cari_data(self):
        ('+---{  MASUKAN NAMA DARI DATA YANG AKAN DI CARI  }--+\n')
        input_nama  = nama()
        view.cari(self)
    
    def keluar(self):
        print('\n\033[97m=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: A. Reza Baehaqa Jamroni\nKelas\t: TI.21.C5\nNIM\t: 312110494")
        print(21*'=')