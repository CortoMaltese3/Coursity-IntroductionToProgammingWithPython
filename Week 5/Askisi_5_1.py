#Άσκηση 5.1: Στατιστική
import random
import math

def stats(L):
    Sum = 0
    for i in range(N):
        Sum = Sum + L[i]       
    M = Sum / N

    dt = 0
    for i in range(N):
        dt = dt + math.pow((L[i] - M), 2)       
    sd = math.sqrt(1/(N-1)*dt)

    print("Πλήθος ακεραιων στη λίστα:", len(L))
    print("Λίστα: ", L)
    print("Μέσος όρος = {}, Τυπική απόκλιση = {}".format(M, sd))

    return

N = int(input("Καταχώρησε πόσες τιμές Ν θες να έχει η λίστα: "))

L = [random.randrange(1,21,1) for i in range(N)]

stats(L)


    
    
