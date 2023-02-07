print("""****************
Kullanici girisi
****************""")

sys_kullanici_adi = "murat"
sys_parola = "12345"

kullanici_adi = input("ad: ")
parola = input("parola: ")

if(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Parolanız hatalidir.")
elif(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanici adiniz hatalidir.")
elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanici adiniz ve sifreniz hatalidir.")
else:
    print("Basariyla giris yaptiniz.")