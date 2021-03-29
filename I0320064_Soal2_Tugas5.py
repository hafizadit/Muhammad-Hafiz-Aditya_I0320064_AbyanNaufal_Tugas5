# Header
print("")
print("="*50)
end = "Program Konversi Nilai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

# Input
nama = input("Masukkan nama anda :")
nama = nama.title()
nilai = float(input("Masukkan nilai anda :"))

# If
if nilai >= 85:
    konversi = "A"
    print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
elif nilai >= 80:
    konversi = "A-"
    print("\nHalo %s! Nilai anda setelah dikonversi adalah"%nama, konversi)
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

# Footer
print("")
print("="*50)
end = "Program Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
