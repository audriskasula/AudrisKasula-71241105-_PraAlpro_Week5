def cek_angka(bil1, bil2, bil3) :
    if bil1 != bil2 != bil3 :
        if bil1 + bil2 == bil3 or bil2 + bil3 == bil1 or bil1 + bil3 == bil2 :
            return True
        else : return False
    else : return False
print(cek_angka(1, 2, 2))