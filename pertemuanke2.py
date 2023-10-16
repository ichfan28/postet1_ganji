print("pilih mata uang yang mau dikonversikan")
print("1.USD")
print("2.YEN")
print("3.MYR")

pilih_pengguna=input("pilih mata uang mana yang ingin dikonversikan: (1/2/3): ")

nilai_usd= 14000
nilai_yen= 130
nilai_myr= 3300

jumlah_rupiah= float(input("Masukan jumlah rupiah: "))

if pilih_pengguna == "1":
    jumlah_mata_uang=jumlah_rupiah / nilai_usd
    print(f"hasil konversi:{jumlah_rupiah} IDR = {jumlah_mata_uang} USD ")

elif pilih_pengguna == "2":
    jumlah_mata_uang=jumlah_rupiah / nilai_yen
    print(f"hasil konversi:{jumlah_rupiah} IDR = {jumlah_mata_uang} Yen ")

elif pilih_pengguna == "3":
    jumlah_mata_uang=jumlah_rupiah / nilai_myr
    print(f"hasil konversi:{jumlah_rupiah} IDR = {jumlah_mata_uang} Ringgit ")

else:
    print("Angka tidak valid, mohon isi dengan (1/2/3)")
