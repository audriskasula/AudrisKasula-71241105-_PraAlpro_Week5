konversi_suhu_fahrenheit = lambda celcius : (9/5) * celcius + 32
konversi_suhu_reamur = lambda celcius : 0.8 * celcius

konversi = str(input("konversi celcius ke?(f/r): "))
celsius = int(input("masukan suhu celcius: "))

konversi = F"F = {int(konversi_suhu_fahrenheit(celsius))}" if konversi == "f" else f"R = {int(konversi_suhu_reamur(celsius))}" if konversi == "r" else "konversi tidak tersedia"

print(konversi)