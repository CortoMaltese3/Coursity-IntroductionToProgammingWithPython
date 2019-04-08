#Άσκηση 6.2: Έλεγχος αρχείου εικόνας

checkType = []
try :
    with open('imag', 'rb') as binfile:
        data = binfile.read()
        bdata = bytearray(data)
        
        for i in range(3):
            print(i+1, 'byte||', 'hexadecimal:', hex(bdata[i]), 'decimal:', int(str(hex(bdata[i])), 16) )
            checkType.append(int(str(hex(bdata[i])),16))

        if (checkType[0] == 255 and checkType[1] == 216 and checkType[2] == 255) :
                print('Το αρχείο ΔΕΝ ειναι τύπου .jpg')

except FileNotFoundError :
    print('Σφάλμα: Δεν υπάρχει το αρχείο σε αυτή τη θέση')
