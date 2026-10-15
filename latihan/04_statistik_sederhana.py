def statistik(data):
    nilai_minimum = min(data)
    nilai_maksimum = max(data)
    rata_rata = sum(data) / len(data)

    return nilai_minimum, nilai_maksimum, rata_rata


angka = [80, 75, 90, 85, 70]

minimum, maksimum, rata_rata = statistik(angka)

print("Nilai minimum:", minimum)
print("Nilai maksimum:", maksimum)
print("Rata-rata:", rata_rata)