'''
What is a User define function?
How many kind of user function there are?
What is user defined function is necessary?

Defination: A user defined function is a block of reusable code that user can
create with a set of parenthesis after the function name.
It is preceded by a 'def' keyword & followed by a set of parenthesis with colon.

There are 4 type of defined function:
1. The one where no argument given & no return initiated.
2. The one where argument given & no return initiated.
3. The one where no argument given & return initiated.
4. The one where argument given & return initiated.

When a program gets bigger and complicated, a programmer can only use the user defined
function to execute block of code and inputting data if applicable without repeating the entire
block of code.

Q.what is an argument in a user defined function?
The data we input in a UDF calling the function

What is a parameter in a user defined function?
Argument in UDF need a matching set of a variable  to call out the function. These are called parameter.

What is f string in python?
f string are called 'formatted string literals' introduced with python 2.6 which made formatting much easier.
'''

# def happy_birthday(name,birthday_age): #parameter (name,birthday_age)
#     print('Happy Birthday to',name.title().strip())
#     print(f'You are old {birthday_age} old')
#     print(f'Here comes {birthday_age} kicked before we throw you in the pool')
# happy_birthday('arif', 40)
# happy_birthday('hasan', 30)

'''

class ex:
Dhaka city utility wants to update their invoice reporting. They want the privilege to just type a UDF & argument 
to automatically send a text to customer as follow:

Hello Mr./Ms. Dilara Akhter
Your city ID is 454
Your Total bill is 1234.56 Taka

Write the code with a UDF, argument and parameter to facilitate such privilege in Dhaka city website.
Submit 3 ss. One for code, two for different arguments. 
'''
#
# def invoice_reporting(name,ID,bill):
#     print(f'Hello {name.strip().title()}')
#     print(f'Your city ID is {ID}')
#     print(f'Your Total bill is {bill}')
#
# invoice_reporting("Dilara Akhter",454, 1234.56)
# invoice_reporting("Maksudur Rahman",656, 5678.90)


#
# def score_revel(name,id):
#     print(f"Hi {name.title().strip()}")
#     print(f"Based on your id {id}")
#     print("You are qualified for the session.")
#
# name=(input('Enter Your name:'))
# id=int(input('Enter Your ID:'))
# score_revel(name,id)

