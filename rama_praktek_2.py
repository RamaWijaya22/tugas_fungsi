#Nama           :Rama wijaya
#Kelas          :XI-TKJ 1
#Nomor Absen    :22
#Soal           :Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.
#Rumus          :Faktorial n = n * (n-1) * (n-2) * ... * 1

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
hasil = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah: {hasil}")
