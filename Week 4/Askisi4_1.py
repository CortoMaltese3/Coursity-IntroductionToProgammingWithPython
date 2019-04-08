#Άσκηση 4.1: Ονόματα & Αριθμός Μητρώου

userInputList = []
userInputBreakElements = []
userInputDictionary = {}

print("Ονόματα & Αριθμός Μητρώου".center(50," "))
print("Καταχώρηση ονόματος και αριθμού μητρώου σε λεξικό.\nΓια να τερματίσεις την εφαρμογή πληκτρολόγησε 'q'")
userInput = input("Καταχώρησε τον ΑΜ σου και το όνομά σου, χωρισμένα με κόμμα(,) : ")


while userInput != 'q':

    userInputBreakElements = userInput.split(',')
    userInputBreakElements[0] = int(userInputBreakElements[0])
    userInputList.append(userInputBreakElements)
    userInput = input("Καταχώρησε τον ΑΜ σου και το όνομά σου, χωρισμένα με κόμμα(,) : ")
    

userInputDictionary = dict(userInputList)
userInputDictionary = dict(sorted(userInputDictionary.items()))

print("\nΠεριχόμενα λεξικού :" )

for key,value in userInputDictionary.items() :
    print("{} {}".format(key,value))

