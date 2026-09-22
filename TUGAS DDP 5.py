def biayaKamar(jenisKamar, lamaNginap):
    if jenisKamar.lower() == "deluxe":
        tarif = 350000
    elif jenisKamar.lower() == "standard":
        tarif = 200000
    else:
        tarif = 0
        print("Jenis kamar tidak dikenali.")

    totalBiaya = tarif*lamaNginap
    return totalBiaya

print("---PEMESANAN KAMAR HOTEL ABC---")
while True:
    jenisKamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
    if jenisKamar.lower() == "standard" or jenisKamar.lower() == "deluxe":
        break
    else:
        print ("Jenis kamar tidak dikenali")

tanggal_checkin = input("Masukkan tanggal check-in: ")

tanggal_checkout = input("Masukkan tanggal check-out: ")

while True:
    lama_menginap = input("Masukkan lama menginap (malam): ")
    if lama_menginap.isdigit and int(lama_menginap) >0:
        lamaNGINAP = int(lama_menginap)
        break
    else:
        print("Input tidak valid, mmasukkan angka lebih dari 0!")

totalBiaya = biayaKamar(jenisKamar,lamaNGINAP)
print("--- Rincian Pemesanan Hotel ---")
print("Jenis Kamar     :", jenisKamar)
print("Check-in        :", tanggal_checkin)
print("Check-out       :", tanggal_checkout)
print("Lama Menginap   :", lamaNGINAP, "malam")
print("Total Biaya     : Rp", totalBiaya)