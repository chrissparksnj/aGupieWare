# https://ia600801.us.archive.org/7/items/MIT6.00SCS11/MIT6_00SCS11_lec03_300k.mp4
# 19:25


## find the cube root of a perfect cube

# What values are gurantee to stop the program?
""" All values of x"""

# Decrementing Function
# 1. map set of program variables to an integer.
# 2. when loop is entered for the first time, it's value is non-negative
# 3. when it's value LT or EQ to 0, loop terminates.
# 4. it's decreased each time through the loop.

# ABS(X) - ANS**3
#x = 8; 8 - 0 = 8; 8 - 1 = 7 

#Exhaustive enumeration

'''
x = int(input("Enter an integer: "))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    #print("Current guess = ", ans)
if ans*ans*ans != abs(x):
    print(x, " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("CUBE Root of " + str(x) + " is " + str(ans))

'''


## Program abstraction
## range function returns tuple(x, y - 1)
## break exits the inner most loop for nested for loops
'''
x = int(input("Enter an integer: "))
ans = 0
for ans in range(0, abs(x) + 1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print(x, " is not a perfect cube ")
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))
'''
## Approximation - finding answer that is good enough
## Define how good of a approximation were willing to accept
## Find a y such that y * y = x +/- Epsilon

x = 25
epsilon = 0.01
numGuesses = 0
ans = 0.0

while abs(ans**2 -x) >= epsilon and ans <= x:
    ans += 0.00001
    numGuesses +=1
print("Numguesses = ", numGuesses)

if abs(ans**2 - x) >= epsilon:
    print("Failed on the sqroot of", x)
else:
    print(ans, " is close to the sqroot of", x)
    













