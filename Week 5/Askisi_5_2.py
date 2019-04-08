#Άσκηση 5.2: Συνάρτηση Γεννήτορας

def myrange(N,logos):
    geom_prog = 1
    i = 1
    while i <= N:
        yield geom_prog
        geom_prog = geom_prog * logos
        i += 1  

for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)
