##Bubble sort

##reads an integer N and creates a list L, with N random numbers in range [1,100]
##then uses the bubble sort to sort the list and print it. 

import random


N = int(input("Give me an integer N: "))
L = []

L = [random.randrange(1,101,1) for i in range(N)]
        
print("The list L contains the following ", N, " numbers:\n", L, sep='')

for i in range(0,N-1,1):
    for j in range(0,N-1-i,1):
        if L[j+1] < L[j]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp
            
print("The elements of the list L, bubble sorted are :\n", L, sep = '')
