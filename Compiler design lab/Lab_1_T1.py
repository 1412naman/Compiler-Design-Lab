#Set of all strings over the binary alphabet containing an even number of a’s and an even number of b’s.

def BinaryString(s):
    count_a = 0
    count_b = 0

    for char in s:
        if char == "a":
            count_a += 1
        elif char == "b":
            count_b += 1

    return count_a % 2 == 0 and count_b % 2 == 0


n = input("Enter the string: ")
if BinaryString(n):
    print(f"'{n}' satisfied and implemented ")
else:
    print(f"'{n}' invalid string ")
