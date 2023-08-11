#Set of all strings ending with two symbols of the same type. 

def StringSet(s):
    if len(s) < 2:
        return False
    last_two_Symbols = s[-2:]
    return last_two_Symbols[0] == last_two_Symbols[1]

n = input("Enter the string: ")
if StringSet(n):
    print(f"'{n}' Implemented ")
else:
    print(f"'{n}' Invalid string ")    