# Header
print("")
print("="*50)
end = "Program Konversi Nilai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

# Fungsi
def nilaiKonversi():
    nama = input("Masukkan nama anda :")
    nama = nama.title()
    nilai = float(input("Masukkan nilai anda :"))
    if nilai > 100:
        print(""""Maaf, nilai yang anda masukkan salah.
        Silakan Mengulang!""")
        nilaiKonversi()
    elif nilai >= 85:
        konversi = "A"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    elif nilai >= 80:
        konversi = "A-"
        ("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    elif nilai >= 75:
        konversi = "B+"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    elif nilai >= 70:
        konversi = "B"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    elif nilai >= 65:
        konversi = "C+"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    elif nilai >= 60:
        konversi = "C"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
    else:
        konversi = "E"
        print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)

nilaiKonversi()

# Footer
print("")
print("="*50)
end = "Program Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
