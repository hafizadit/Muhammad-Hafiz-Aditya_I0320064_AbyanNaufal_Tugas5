# Header
print("")
print("="*50)
end = "Program Sapa"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

# Program
nama = input("Masukkan nama anda :")
LK = input("Masukkan jenis kelamin anda (l/p) :")
print("")

if LK == "l" or "L":
    print("Selamat datang, Tuan",nama)
elif LK == "p" or "P":
    print("Selamat datang, Nyonya",nama)

# Footer
print("")
print("="*50)
end = "Program Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")
