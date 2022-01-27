import random
import os, time

# Luodaan noppa ja silmäluvut silleen kivasti
def teeNoppa():
    numero_1 = ("     \n"
                "  o  \n"
                "     \n")

    numero_2 = ("    o\n"
                "     \n"
                "o    \n" )    

    numero_3 = ("    o\n"
                "  o  \n"
                "o    \n")

    numero_4 = ("o   o\n"
                "     \n"
                "o   o\n")

    numero_5 = ("o   o\n"
                "  o  \n"
                "o   o\n")

    numero_6 = ("o   o\n"
                "o   o\n"
                "o   o\n")
    
    noppa = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6]
    return noppa

# Nopan heittoa, visualisoidaan nopan pyörimistä hieman ja annetaan joku silmäluku
def heitaNoppaa(noppa):
    random_hyrrays = random.randint(3,10)
    for x in range(random_hyrrays):
        os.system('cls')
        randomi_numero = random.randint(0, 5)
        print(noppa[randomi_numero])
        time.sleep(0.3)


# Pääohjelma, jossa luodaan noppa ja viskotaan sitä kunnes käyttäjä ei enää jaksa
def main():
    noppa = teeNoppa()
    while(True):
        vastaus = input("heitetäänkö?(y/n)> ")
        if vastaus == "n":
            break
        if vastaus == "y":
            heitaNoppaa(noppa)
        else:
            continue

        
 

if __name__=="__main__":
    main()





