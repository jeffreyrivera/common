#Lets start easy
def suma(n):
    if (n<=0):
        return 0
    else:
        return n + suma(n-1)
        
#serious now   
def fib(n):
    if n <= 1: 
        return n
    else: 
        return fib(n-1)+fib(n-2)

seq = fib(9)
print(seq)

# dynamic, in place 0(n)
def fib2(limit):
    i = 0
    seq = [i]*limit
    for fib in range(0,limit):
        if (fib == 0 or fib == 1):
            seq[fib] = fib
        else:
            seq[fib] = seq[fib-1] + seq[fib-2]
    return seq

seq = fib2(20)
print(seq)

# sum first 20
print(sum(seq))