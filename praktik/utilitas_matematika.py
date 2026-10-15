def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas Persegi Panjang")
    print("2. Luas Segitiga")
    print("3. Jumlah Bilangan 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        try:
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))

            if p < 0 or l < 0:
                print("Panjang dan lebar tidak boleh negatif.")
            else:
                print("Luas persegi panjang:", luas_persegi_panjang(p, l))
        except ValueError:
            print("Input harus berupa angka.")

    elif pilihan == "2":
        try:
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))

            if a < 0 or t < 0:
                print("Alas dan tinggi tidak boleh negatif.")
            else:
                print("Luas segitiga:", luas_segitiga(a, t))
        except ValueError:
            print("Input harus berupa angka.")

    elif pilihan == "3":
        try:
            n = int(input("Masukkan bilangan n: "))

            if n < 0:
                print("n tidak boleh negatif.")
            else:
                print("Jumlah bilangan:", jumlah_n(n))
        except ValueError:
            print("Masukkan bilangan bulat yang benar.")

    elif pilihan == "4":
        try:
            n = int(input("Masukkan bilangan n: "))

            if n < 0:
                print("n tidak boleh negatif.")
            else:
                print("Hasil faktorial:", faktorial(n))
        except ValueError:
            print("Masukkan bilangan bulat yang benar.")

    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1 sampai 5.")