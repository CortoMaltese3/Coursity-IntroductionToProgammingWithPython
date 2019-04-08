#Άσκηση 4.2: Λέξεις του Scrabble

userInput = ''
wordList = []
letterList = []
pointDictionary = {}
points_1 = ['Α', 'Ε', 'Η', 'Ι', 'Ν', 'Ο', 'Σ', 'Τ']
points_2 = ['Κ', 'Π', 'Ρ', 'Υ']
points_3 = ['Λ', 'Μ', 'Ω']
points_4 = ['Γ', 'Δ']
points_8 = ['Β', 'Φ', 'Χ']
points_10 = ['Ζ', 'Θ', 'Ξ', 'Ψ']

print("**Λέξεις του Scrabble**".center(100," "))
print("Το πρόγραμμα δέχεται ελληνικά, κεφαλαια γράμματα, χωρίς τόνους και επιστρέφει τους πόντους της λέξης")

userInput = input("Καταχώρησε τη λέξη σου ή πληκτρολόγησε 'q' για έξοδο: ")

while userInput != 'q':
    points = 0
    wordList.append(userInput)
    
    if userInput == 'q':
        wordList.pop()
        
    letterList = list(userInput)

    for letter in letterList:
        if letter in points_1:
             points += 1
        elif letter in points_2:
             points += 2
        elif letter in points_3:
             points += 3
        elif letter in points_4:
             points += 4
        elif letter in points_8:
             points += 8
        elif letter in points_10:
             points += 10
    
    print("Η λέξη {} που διάλεξες αξίζει {} πόντους! ".format(userInput, points))
    pointDictionary[userInput] = points

    userInput = input("Καταχώρησε τη λέξη σου ή πληκτρολόγησε 'q' για έξοδο: ")
    
print()
pointDictionary = dict(sorted(pointDictionary.items()))

for word,points in pointDictionary.items() :
    print("{} {}".format(word,points))


#Σημειωση : Δεν έχει γίνει έλεγχος αν μπει μη-επιτρεπτή λέξη από το χρήστη

