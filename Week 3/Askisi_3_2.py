#Άσκηση 3.2: Ουρά δύο άκρων

print("Οδηγίες: Το πρόγραμμα καταχωρει αριθμους σε μια λίστα! Τρέχει σε άπειρο βρόχο, έως ότου πληκτρολογήσεις 'q'. \nΑν θελήσεις να βγάλεις το πρώτο στοιχείο της λίστας, πληκτρολόγησε '0r' ενώ,\nαν θέλεις να βγάλεις το τελευταιο, πληκτρολόγησε 'r'\n  ")

newNumber = input("Για να ξεκινήσεις, πάτησε Enter \n")
alist = []
check = True

while check == True :
    
    newNumber = input("Δώσε μου τη καταχώρηση σου: ")
    if newNumber != 'q' and newNumber != 'r' and newNumber != '0r' :
        if newNumber[0] != '0' :
            alist.append(float(newNumber))
            check = True                   
        else :
            numberToList = list(newNumber)
            numberToList.pop(0)
            listToNumber = ''.join(numberToList)
            alist.insert(0, float(listToNumber))
            check = True
        print(alist)

    
    elif newNumber == 'r':
        print("\n*****Από τη λίστα βγήκε το τελευταίο στοιχειο*****", alist[(len(alist) - 1)])
        alist.pop((len(alist))-1)
        print(alist)
        check = True
    elif newNumber == '0r' :
        print("\n*****Από τη λίστα βγήκε το πρώτο στοιχειο*****", alist[0])
        alist.pop(0)
        print(alist)
        check = True
     
    else:
        print("\nΤέλος εφαρμογής!")
        check = False

    
#παρατηρήσεις :
#1) Στο πρόγραμμα δεν έχει μπει κάποιος έλεγχος για την εισοδο του χρήστη κι έτσι αν πληκτρολογήσει κάτι εκτος από αριθμό ή 'q' / 'r' / '0r' το πρόγραμμα σκάει
#2) Ο έλεγχος με το 'r', '0r' έγινε εκτός της πρώτης εισόδου για να συμπεριλάβουμε τη περίπτωση που η λίστα ειναι κενή. Αντίστοιχα η εκτέλεση του προγραμματος
    #θα βγάλει σφάλμα αν παω να αφαιρέσω και το τελευταιο στοιχειο της λίστας και πατήσω 'r' ή '0r'

