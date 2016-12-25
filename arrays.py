# 1.Implement and algorithm if String has all unique characters. What if you cannot add and additional data structute
# Brute force is O(n^2)
# Hash table add char as key if key exist not unique O(N)
def stringUnique(str):
    #Common Cases
    if len(str)<2:
        return True
    elif str is None:
        return False
    elif len(str)>128:
        return False
        
    unique = dict()
    for ch in str:
        if ch in unique:
            return False
        else:
            unique[ch]=1
    return True
#each string is it ASCII Unicode each character has a unique code 0-127 O(N)
def stringUnique2(str):
    #Common Cases
    if len(str)<2:
        return True
    elif str is None:
        return False
    elif len(str)>128:
        return False

    unique = [False]*128
    for ch in str:
        code = ord(ch)
        if unique[code] == False:
            unique[code] = True
        elif unique[code] == True:
            return False
    return True
    
#Example
# print (stringUnique("calros"))
# print (stringUnique2("calros"))
# print (stringUnique("caaa"))
# print (stringUnique2("sasfdv asdasdd"))


# Prob2. Give two strings , write a method to decide if one is a permutation of the other

def checkPerm(a,b):
    if (a is None or b is None):
        return False
    elif len(a) != len(b):
        return False
    else:
        return sorted(a) == sorted(b)


print (checkPerm("calros", "alrosc"))
print (checkPerm("calros", "alroscs"))
print (checkPerm("calros", "alroscsds"))
print (checkPerm("calros", None))
print (checkPerm(None, "asdsad"))

