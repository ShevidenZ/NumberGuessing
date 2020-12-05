import random

def main():
    print("Hai Coba tebak angka berapa yang ada di otakku, dari 1 sampai 10")
    angkanya = random.randrange(1, 10)
    
    Percobaannya = 1
    
    Tebakan = 0
    
    while Tebakan != angkanya and Percobaannya <3:
        print("Percobaan ke-",Percobaannya)
        yang_kalian_ketik = input("Coba Sebutkan Angka yang ada di otakku\n")
        Tebakan = int(yang_kalian_ketik)
        
        if Tebakan > angkanya:
            print("Lebih Rendah")
        elif Tebakan < angkanya:
            print("Lebih Tinggi")
        else:
            print("Kamu Benar!")

        Percobaannya += 1
        
    if Tebakan != angkanya:
        print("Sepertinya kamu kebahisan peluang. angkanya adalah " + str(angkanya) +".")
    
main()
