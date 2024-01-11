

'''
Class Exercise: 01
Write a python program asking user to enter his or her age. The code should have > and == operator. The conditions are:
1. The user should be eligible to join army if greater than a certain age
2. Eligible for Army pre training if equal to certain age
3. Otherwise, not eligible to join army.

Submit 4 screenshots (1 code, 3 output showing 3 possible outcomes)
'''

#
# age=int(input("What is your age: "))
#
# if age > 18:
#     print("Your are eligible")
# elif age == 18:
#     print("You have to do pre-traning")
# else:
#     print("You are not eligible")





# age=int(input("Enter your age:"))
#
# if age>18:
#     print("Your are eligible to join army!")
# elif age==18:
#     print("Your are eligible for Army pre training!")
# else:
#     print("Your are not eligible to join army!")


'''
Class Exercise: 02
BCB wants to facilitate Asia Cup ticket selling on its website with some new conditions.
The new rules are:
1. Anyone greater or equal to age 11 is eligible to watch a match.
2. If eligible, the price of tickets is $12, when the age is
less than or equal to 20 or greater than or equal to 60. Otherwise
the ticket price is $25.
Write the python code that should be part of the BCB website update.

Submit 4 screenshots (1 code, 3 output showing 3 possible outcomes)
'''

# age=int(input("Enter your age:"))
#
# if age >=11:
#     print("You are eligible to watch the match!")
#     if age <=20 or age >=60:
#         print("Your ticket price is $12!")
#     else:
#         print("Your ticket price is $20!")
#
# else:
#     print("You are not eligible to watch the match!")














# age=int(input("Enter your age:"))
#
#
# if age>=11:
#     print("You are eligible to watch the match! ")
#     if age<=20 or age>=60:
#         print("Your ticket price is $12")
#     else:
#         print("Your ticket price is $25")
# else:
#     print("You are not eligible to watch the match live!")


'''
Class Exercise 03:
An air ticket website is asking users to enter children’s age to validate passenger seat availability. The conditions are:
1. If the children is 2 or more years old, the child is eligible for a passenger seat. Otherwise, the child must fly strapped to a parent.
2. If the child is 4 or less years old, and 3 or less feet in height, the child must use a baby seat belt. Otherwise, the child can use a regular seat belt.

Write a python code that should be part of the air ticket website.

Submit 5 screenshots.[One for Code, rest for the following age and height data.
Age = 3.5, height = 3; Age = 4.1, height = 3; Age = 4, height = 3; Age = 4.1, height = 3.1

# '''
#
# age=float(input("Enter your age:"))
# height=float(input("Enter your height:"))
#
# if age>=2:
#     print("The child is eligible for a passenger seat.")
#     if age<=4 and height<=3:
#         print("The child must use a baby seat belt!")
#     else:
#         print("The child can use a regular seat belt!")
# else:
#     print("The child must fly strapped to a parent.")

'''
Class Exercise 04:
A car rental website is asking user to enter his or her age to validate renting eligibility.
The conditions are:
1. If the driver is 25 or more years old, the driver is eligible to rent.
Otherwise, not eligible to rent.
2. If the driver's age is 30 or less AND driving experience is 10 years or less,
a deposit of $1000 is required. Otherwise, no deposit required.
Write the python code that should be part of the car rental company's website.

Submit 4 screenshots.[One for Code, rest for the following age and height data.

Age 0 to 24 for not eligible
25 to 30/0 to 10 for $1000 deposit required
31 or more/11 or more for no deposit

'''


# age=float(input("Enter your age:"))
# experience=float(input("Enter your year of experience:"))
#
# if age>=25:
#     print("You are eligible to rent.")
#     if age<=30 and experience<=10:
#         print("$1000 deposit is required!")
#     else:
#         print("No deposit is required!")
# else:
#     print("You are not eligible to rent.")


'''
Class Exercise 05:
Your company loves to give bonuses but it has certain conditions. You need to input your salary
and years of experience on the website. 
The conditions are:
1. If your years of experience is greater than or equal to 1 and less than or equal to 5,
Then your bonus is 5% of your salary.
2. If your years of experience is greater than or equal to 6, 
then your bonus is 8% of your salary.
If the above two conditions are not met, you are not eligible for bonus.

# This example will clears when it is ideal to use elif. Ideally, we should use elif when the range of block of code
above has no relation with the block of code below.
'''

# salary = float(input("Enter your salary: "))
# yoe = float(input("Enter your experience: "))
#
# if yoe >= 1 and yoe <= 5:
#     print("Your bonus is:", str(salary*.05))
# elif yoe >= 6:
#     print("Your bonus is:", str(salary * .08))
# else:
#     print("You are not eligible for the bonus!!")




#
# def birthday(name,age):
#     print(f"Happy Birthday {name.strip().title()}!!")
#     print(f"You are now {age} years old!!")
#
# birthday('maruf hAsan arif',25)
# birthday('Maksudur Hahman',26)


# name=input("Enter Your name:")
# loyaltyID=int(input("Enter Your Id:"))
# bonus_point=float(input("Enter your bonus point:"))
#
# discount=346*.04
#
# print(f"Hello{name.strip().title()} Thank you for being a loyal customer of Herfy.")
# print(f"Based on your loyaltyID of{loyaltyID}")
# print(f"You purchase of 346 USD can get a discount of 4%, which is{discount}")
# print(f"And your current bonus point is{bonus_point}")


# name=input("Enter Your name:")
# ticketID=int(input("Enter Your ticketId:"))
# Aircraft_name=input("Enter Your aircraft_name:")
# ticket_price=float(input("Enter your ticket price:"))
#
# credit=ticket_price*.02
#
# print(f"Hello{name.strip().title()} Thank you for being a frequent flyer.")
# print(f"Based on your Ticket ID of {ticketID}")
# print(f"Your aircraft {Aircraft_name} airlines flight will depart at 10 a.m.")
# print(f"And your ticket price  of {ticket_price} has been given a 2% credit of {credit} USD.")

# gpa = float(input("What is your Gpa:"))
# publication = int(input("What is your publication number:"))
# if gpa >= 2.8:
#     print("Eligible for register for the seminar")
#     if gpa < 3.5 and publication < 3:
#         print("The price of scholarship application is $70")
#     else:
#         print("The price of scholarship application is $7")
# else:
#     print("You are ineligible to apply!")

# def DCC(name,age,height):
#     print(f'Hello Mr. {name}')
#     print(f'You are {age} years old'
#           f'And your height is {height}')
#
# DCC('Ml Jak',30,5.6)
# DCC('Arif Hasan',40,6.2)


# ans=input('What do you mean by statement?')
# ans_2='Executable line in a program is called instruction'
# if ans==ans_2:
#     print(101)
# else:
#     print(404)



# def addition():
#     additionvalue1=int(input("Enter the tip value:"))
#     additionvalue2 = int(input("Enter the vat value:"))
#     print(f'The total charge calculated to {additionvalue1+additionvalue2} Taka')
# addition()

'''
Variable created in UDF can only be reused in any other function or with out function, if the return key was initiated.
'''

# def add():
#     salary=float(input("Enter your salary:"))
#     tax=salary*.06
#     print(f'Your income tax is $ {tax}')
# add()


# --------------3. No Arguments Given, Return Initiated-------------


# def multiplication():
#     multiplication_01 = int(input("Enter the total amount of your FDR:"))
#     multiplication_02 = float(input("Enter the interest rate:"))
#     multi_result = multiplication_01*multiplication_02
#     return multi_result # the result is stored in return keyword now
#
# multi_result = multiplication()  # Transfering the result stored in return keyword to the function by equaling both & function is called
# print(f'Your FDR is $ {multi_result}')



# def eligibility():
#     credit_hours=int(input("Enter your Credit hours: "))
#     gpa = float(input("Enter your gpa: "))
#     multi_calcu = credit_hours * gpa
#     return multi_calcu
# multi_calcu=eligibility()
#
# if multi_calcu >=400:
#     print("Your are eligible for internship!")
# else:
#     print("Your are not eligible for internship!")


# 3.----------Arguments Given, and Return Is Also Initiated=--------

# def substraction(subvalur1,subvalue2):
#     print(f'The total discount calculates to {subvalur1-subvalue2} taka \n ')
# substraction(200,80)
# substraction(300,60)


# def eligibility(influenza_01,influenza_02):
#     if influenza_01 >=60 and influenza_02>=60:
#         print('You are eligible for chicken pox immunization')
#     else:
#         print('You are  not eligible for chicken pox immunization')
# eligibility(40,80)
# eligibility(70,79)


# ------------Arguments Given, and Return Is Also Initiated---------

# def Divition(divisitionvalue01,divisitionvalue02):
#     return divisitionvalue01/divisitionvalue02
# division_value=Divition(20,70)
#
# print(f'The value is {division_value}')


# def Divition(divisitionvalue01,divisitionvalue02):
#     return f'Last Semester I used ChatGpt {round(divisitionvalue01/divisitionvalue02)} times'
# division_value=Divition(300,70)
#
# print(division_value)

# def paper(publictions,years):
#     return f'On average, the faculty is publishing {round(publictions/years)}'
# paper_publication=paper(30,4)
# print(paper_publication)


# def mortgage():
#     asset_value=float(input("Enter your asset value: "))
#     interest= float(input("Enter your interest %: "))
#     print(f'Your monthly mortgage is {round(asset_value*interest)}')
# mortgage()

# def GRE():
#     verval=int(input("Enter your verval score: "))
#     analytical= int(input("Enter your analytical score: "))
#     quantitative = int(input("Enter your quantitative score: "))
#     sum=verval+analytical+quantitative
#     return sum
# sum=GRE()
#
# if sum >=320:
#     print("You are eligible to apply for scholarship at UBC!!")
# else:
#     print("You are not eligible to apply for scholarship at UBC!!")

# def DHE(weight):
#     if weight >= 2000:
#         print('The Toll is 150tk')
#     else:
#         print('The Toll is 80tk')
# DHE(4000)

# def publication(publiction,year):
#     sum=publiction/year
#     return sum
# sum=publication(20,4)
# print(f'Based on the data,the faculty is publishing {round(sum)} papers on average per year. ')
#



# cgpa=float(input("Enter your cgpa: "))
#
# math=int(input("Enter your math score: "))
# bangla=int(input("Enter your bangla score: "))
# english=int(input("Enter your english score: "))
#
# average=(math+bangla+english)/3
# print(f"Based on your average score {average}, you are eligible to ge 20% waiver!")


# arguments given and return is not given
# def happy_birthday(name,age):
#     print(f'Happy Birthday {name},\n'
#           f'you are now {age} years old.')
#
# happy_birthday('arif',20)

#
# def utility(name,city_id,bill):
#     print(f'Hello {name.strip().title()}' )
#
# utility('    asif',333,434)



# def add():
#      weather = float(input('enter the weather:'))
#      result = weather*(9/5)+32
#
#      return result
#
# result = add()
#
# print(f'the weather of dallas this morning is {result}')

#arguments, return
#


# def add1(weather):
#        value=  weather*(9/5)+32
#        return weather
# value  = add1(30)
#
# print(f'the weather of dallas this morning is {result}')









# --------------4 types of UDF-------------------


'''
Arguments given and return given
'''

# def C_TO_F(celsius):
#     fahrenheit=celsius*(9/5)+32
#
#     return fahrenheit
# fahrenheiht=C_TO_F(40)

print(f'The weather of Dallas this morning is {round(fahrenheiht)} in Fahrenheit.')


'''
Arguments given and return is not given
'''

# def C_TO_F(celsius):
#     fahrenheit=celsius*(9/5)+32
#     print(f'The weather of Dallas this morning is {fahrenheit} in Fahrenheit.')
# C_TO_F(90)


'''
Arguments not given and return given
'''

# def C_TO_F():
#     celsius=float(input("Enter value:"))
#     fahrenheit=celsius*(9/5)+32
#     return fahrenheit
# fahrenheit=C_TO_F()

# print(f'The weather of Dallas this morning is {round(fahrenheit)} in Fahrenheit.')

'''
Arguments not given and return not given
'''


# def C_TO_F():
#     celsius = float(input("Enter value:"))
#     fahrenheit=celsius*(9/5)+32
#     print(f'The weather of Dallas this morning is {round(fahrenheit)} in Fahrenheit.')
# C_TO_F()
