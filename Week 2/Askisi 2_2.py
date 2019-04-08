#Άσκηση 2.2: Ρουλέτα

import random

player_choice = ' '

while player_choice != "q":
    lucky_num = random.randint(0,36)
    

    if lucky_num == 0 :
        print("\n\nΚληρώθηκε το 0")
    else :
        if lucky_num <= 18 :
            print("Κληρώθηκε το", lucky_num, "!!")
            print("Ο αριθμός", lucky_num, "ειναι μικρός (1-18)")
        else :
            print("Κληρώθηκε το", lucky_num, "!!")
            print("Ο αριθμός", lucky_num, "ειναι μεγάλος (19-36)")

    if ((lucky_num >= 1 and lucky_num <= 10 ) or ((lucky_num >= 19) and (lucky_num <= 28))) :
        if lucky_num % 2 == 1:
            print("O αριθμός", lucky_num ,"ειναι κόκκινος")
        else :
            print("O αριθμός", lucky_num ,"ειναι μαύρος")

    else :
        if lucky_num % 2 == 0:
            print("O αριθμός", lucky_num ,"ειναι κοκκινος")
        else :
            print("O αριθμός", lucky_num ,"ειναι μαυρος")

    player_choice = input("\n‘Enter: Επόμενη Κλήρωση,\t‘q’+Enter: Τερματισμός’ " )
    print("\n", "*" * 50, "\n")

    
