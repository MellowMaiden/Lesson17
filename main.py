#Lesson 17:More on nesting

#Example 1:
#ask the user for a number from 1 to 9
x=int(input("Give me a number more than 0 but less than 10:"))
if x>0 and x<10:
    print("Thank you")
else:
    print("Thant is not correct")

#Example 2:
#ask the user for a number from 1 to 9 (But use nested ifs)
x=int(input("Give me a number"))
if x>0:
    if x<10:
        print("thank you")
    else:
        print("That is too big")
else:
    print("That is too small")

#Example 3:
#Ask the user for a number from 1 to 100 BUT is must be even
x=int(input("Give me a number from 1 to 100 but it must be even:"))
if x>=1 and x<=100 and x%2==0:
    print("thank you")
else:
    print("that is not correct")

#Example 4:
#Ask the user for a number from 1 to 100 BUT is must be even, AND you must use NESTING
x=int(input("Give me a number from 1 to 100 but it must be even:"))
if x>=1:
    if x<=100:
        if x%2==0:
            print("Thank you")
        else:
            print("This is not even , it is a odd")
    else:
        print("It is too big")
else:
    print("It is too small")

#Example 5:
#Create a function called H(x), if x is <0  then H(x) is o,
#IF x is 0 then H(x) is 0.5
#If x >0 then H(x) is 1
def H(x):
    if x<0:
        return (0)
    elif x==0:
            return (0.5)
    elif x>0:
        return (1)

#Example 6:
#Check that x is more than 0 and less than 10 but not 7
if x >0 and x<10 and not x==7:
    print("x is good")

#Example 7:
# write a program that a sks if the user is happy
x=input("are you happy?")
x=x.upper()
if x=="yes" or x=="yeah" or x=="of course" or x=="y" or x=="yep":
    print("That is good")
else:
    print("That is bad")



