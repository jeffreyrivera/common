#Lets start easy
def suma(n):
    if (n<=0):
        return 0
    else:
        return n + suma(n-1)
        
x = 10 + suma(10)
print(suma(5))