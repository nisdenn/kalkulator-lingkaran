import math

def hitung_luas(r):
    return math.pi * r**2

def hitung_keliling(r):
    return 2 * math.pi * r

while True:
    try:
        radius_input = input("\nMasukkan jari-jari lingkaran: ")
        radius_input = radius_input.replace(",", ".")
        radius = float(radius_input)

        if radius <= 0:
            print("❌ Jari-jari harus lebih dari 0!")
            continue

    except ValueError:
        print("❌ Input harus berupa angka!")
        continue

    luas = round(hitung_luas(radius), 2)
    keliling = round(hitung_keliling(radius), 2)

    print("\n======================")
    print("     HASIL HITUNG     ")
    print("======================")
    print("======================")
    print("Luas Lingkaran     :", luas)
    print("Keliling Lingkaran :", keliling)
    print("======================")

    ulang = input("\nHitung lagi? (y/n): ")
    if ulang.lower() != "y":
        print("\nTerima kasih")
        break
