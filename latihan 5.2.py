def cek_digit_belakang(bil1, bil2, bil3) :
    cek1 = bil1 % 10
    cek2 = bil2 % 10
    cek3 = bil3 % 10
    if cek1 == cek2 == cek3 :
        return True
    elif cek1 == cek2 or cek2 == cek3 or cek1 == cek3 :
        return True
    else : return False


angka1 = int(input("masukan bilangan pertama: "))
angka2 = int(input("masukan bilangan kedua: "))
angka3 = int(input("masukan bilangan ketiga: "))

print(cek_digit_belakang(angka1, angka2, angka3))