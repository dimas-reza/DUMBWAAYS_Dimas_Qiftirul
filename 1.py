print("    PROGRAM MENGHITUNG JUMLAH BURUNG")
print(" ")

deadrate = 11.1
rasio_kelahiran = 2
daybirth = 21
jumlah_awal = 6969
waktu = 441

#rasio penambahan populasi burung dalam 21 hari
rasio_penambahan = ((100-deadrate)/100)*rasio_kelahiran
print(" Rasio penambahan jumalah setiap 21 hari adalah ", rasio_penambahan)

#Jumlah setelah 441 hari
n = jumlah_awal*(rasio_penambahan**(441/21))
n_integer = int(n)
print(" Jumlah burung setelah 441 hari adalah ", n_integer , "ekor")
