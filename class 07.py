temparature=15

if temparature>16:
    print('You do not need to wear a sweater')
else:
    print('You need to wear a sweater')

'''
Note:
1. In python, whenever we are using conditional keyword such as if, else, elif, nested if else, pythone will auto create an indention
2. The indention is equal to 4 space or equal to a TAB button space. But, its not secessary  to have 4 space. you should have at least 1.
3. Python functions and python keyword must align. For example: if, else, elif should align and print statement should align as well.
4. Indention error & Syntax error: Python only will alarm indention error for the first line under python condition keyword, every other indent error is syntex error.
5. Indention python funtions such as print statement under condition python keyword such as if, else, elif, are call block of code.

'''

Emirate=2146
Qatar= 3312
Biman=2689

if Emirate >Qatar:
    print("Emirates is expensive than Qater")
elif Emirate<Qatar:
    print("Emirates is cheaper than Qater")
elif Biman>Qatar:
    print("Biman is expensive than Qater")
else:
    print("if & elif never ran")


#
# Emirate= 2146
# Qatar= 3312
# Biman= 2689
#
# if Emirate == Qatar:
#     print("Emirates is expensive than Qater")
# elif Emirate==Qatar:
#     print("Emirates is cheaper than Qater")
# elif Biman==Qatar:
#     print("Biman is expensive than Qater")
# else:
#     print("if & elif never ran")


    '''
    Notes on conditional python keyword
    
    1. Python run code line by line. So, whenever we have conditional keyword, forst the "if" 
    statement is checked and "IF" it is true, the python run stops.
    2. elif stands for elseif.
    3.
    '''

    '''
   Class Example:
    Write a python code where you will declear 3 hotels as variables with daily room rate.
    Use if/elif/else keyword to write 3 possibilities. With each possibilities, you must have a print statement such as
    "Sheraton is cheaper than Westin". The "Else" statement should say "No room available at your  price range". In your
    output, the "else" statement should be print.
    '''
#     Sheraton=2000
#     Westin=3000
#     La_meridian=4000
#
# if Sheraton==Westin:
#     print("Sheraton is expencive than Westin")
# elif Sheraton==Westin:
#     print("Sheraton is expencive than Westin")
# elif Sheraton==Westin:
#     print("Sheraton is expencive than Westin")
# else:
#     print("No room available at your  price range")

# Example with input function:

# x=float(input("Enter a value: "))
# if x>5:
#     print('X is grater than 5')
# elif x==5:
#     print('X is Equal than 5')
# else:
#     print('X is less than 5')

'''
 Class exrcise:
 Write a puthon code asking the user to enter his or her height with greater with greater than/less than/equal condition.
 And based on the answers, the user should get a message of " eligible/not eligible to apply for army.
'''

height=float(input("Enter your height:"))

if height > 5.8:
    print("You are eligible to apply for army")
elif height == 5.8:
    print("You are eligible to apply for army")
else:
    print("You are not eligible to apply for army")