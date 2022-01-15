
print('\033[93m==========================================')
print('|   program menambah data dengan class   |')
print('==========================================')
from model.daftar_nilai import *
from view.view_nilai import melihat 
while True:
    data=daftarNilai()
    em=melihat()
    print('\n\033[96mtambah\t(1)\nubah\t(2)\nlihat\t(3)\nhapus\t(4)\ncari\t(5)')                                                                                     
    c = input("\nsilahkan masukan pilihan : ")
    print()
    if (c=="1"):
        data.tambah()
    elif (c=="2"):
        data.ubah()
    elif (c=="3"):
        em.lihat()
    elif (c=="4"):
        data.hapus()
    elif (c=="5"):
        data.cari_data()
    else:
        data.keluar()
        break