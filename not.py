age = 7
# 2-8  $2 ticket
# 65 $5 ticket
# 10 for everyone else

if not ((age >= 2 and age <= 8) or age >= 65):
    print("YOU PAY REGULAR PRICE!!")
else:
    print("YOU ARE A CHILD OR SENIOR")


# Truthy
#x = 0
#y = -1
#(x or y and x )(- 1 == y and y + 1 == x)
# Here it is broken down: x or y # truthy because y is -1 which is a nonzero value; x - 1 == y # true
# because x - 1 is -1, and -1 == -1; x or y and x - 1 == y # true because both sides of the AND are truthy; y + 1 == x # truthy because -1 + 1 does in fact equal zero; x or y and x - 1 == y and y + 1 == x # also truthy because both sides of the second AND are truthy
