#Άσκηση 6.1: Αρίθμηση γραμμών σε αρχείο κειμένου

try :  
    with open('cities.txt', 'r') as infile :
            lineList = infile.readlines()
    with open('out.txt', 'w') as outfile :
            for index in range(len(lineList)):
                outfile.write(str(index + 1)+ ': ' + lineList[index])
except FileNotFoundError :
    print('Σφάλμα: Δεν υπάρχει τέτοιο αρχείο')
except :
    print('Προέκυψε σφάλμα')

