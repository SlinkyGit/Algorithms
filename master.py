# Nikhil Solanki
# Master Theorem

import math

def welcome():
    print("Automated Master Theorem\n")
    print("Enter Formula T(n)=a*T(n/b)+n^x*(log2(n)^y)\n")
welcome()

def var():
    # Inputs from user:
    global a, b, x, y, n, c
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    c = math.log(a, b) # Calculate the c values
var()

def master():
    
    if c > x:
        #Case 1
        print("T(n) = Theta" + "(" + "n^" + str(int(c)) + ")")

    elif c == x:
        #Case 2
        print("T(n) = Theta" + "(" + "n^" + str(int(c)) + ")" + "log2(n)^" + str(int(y + 1)))

    elif c < x:
        #Case 3
        # print("T(n) = Theta" + "(" + "Ω(n^" + str(int(c + 1)) + ")" + ")")
        print("T(n)=Theta" + "(" + "n^" + str(int(c + 1)) + ")")
    

master()
