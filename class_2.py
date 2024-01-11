# Student_Body_at_UIU=7500
# Student_body_text='Total student body at UIU is '
# student=3.5
# GPA=23
# print(type(GPA))
# print(type(student))
#
# print(type(Student_Body_at_UIU))
# print(type(Student_body_text))
#
# print('Total student body at UIU is ' + str(Student_Body_at_UIU))
#
# print(Student_body_text + str(Student_Body_at_UIU))

#Note: When printing, the datatype must match when we are using concat.

#-----------Input Finction---------------

#1. Input function is a requeast for user data.
#2. By default, all variables with input fanctions are of string class.
#
# print('What is your name?')
# Name=input()
# print('Okay, Why did you choose this company?')
# Company=input()
# print('How many years of experience do you have?')
# Experience=input()
# print('What is salary expectation?')
# Salary=input()


# Name=input('What is your name?')
# Company=input('Okay, Why did you choose this company?')
# Experience=float(input('How many years of experience do you have?'))
# Salary=int(input('What is salary expectation?'))
#
# print('Hello'+ Name)
# print('Based on your'+ str(Experience) + 'years of experience,')
# print('And your monthly salary expectation of Taka'+ str(Salary))
# print('We think you need around'+ str(Experience)+'years of admission in a mental hospital')


#Probably Question/Exercise
'''
Write a pythone function with variable declered having input functions based on your final grades for all last semester 
courses and find your average score.
At the end, have a print statement mentioning:
"Based on your average score of ____, You qualify for full tuition waiver."
'''

# Name=input('What is your name?')
# Courses_1=int(input('What score did you get in Principles of Management?'))
# Courses_2=int(input('What score did you get in E-Business?'))
# Courses_3=int(input('What score did you get in Project Management?'))
# Courses_4=int(input('What score did you get in Strategic Management?'))
#
# Score=(Courses_1+Courses_2+Courses_3+Courses_4)/4
#
#
# print('Hello', Name , ', Based on your average score of ' ,Score,  ',You qualify for full tuition waiver.')
#


# Name=input('What is your name?')
# Company=input('Okay, Why did you choose this company?')
# Experience=float(input('How many years of experience do you have?'))
# Salary=int(input('What is salary expectation?'))
#
# print('Hello'+ Name)
# print('Based on your'+ str(Experience) + 'years of experience,')
# print('And your monthly salary expectation of Taka'+ str(Salary))
# print('We think you need around'+ str(Experience)+'years of admission in a mental hospital')

# name=input('What is your name?')
# print("Helloo",name)

# name=input('What is your name?').strip() #remove space before the answer.
# print("Helloo",name)

# name=input('What is your name?').strip().title()
# print("Helloo",name)

# Probably Questions/Exercise:
# 1. Print the following output with different data types declared in variables.
#    Dr. Shuvo Roy, a Bangladeshi Scientist, is the winner of 2021 KidneyX Artificial Kidney prize
#    granted by American Association of Kidney Patients(AAKP), with a prize money of 2.78 million USD.

# winning_year=2021
# winning_prize=2.78
# text_1= "Dr. Shuvo Roy, a Bangladeshi Scientist, is the winner of"
# text_2= "KidneyX Artificial Kidney prize granted by American Association of Kidney Patients(AAKP), with a prize money of"
# text_3= "million USD."
# #
# # print(text_1, str(winning_year), text_2, str(winning_prize), text_3)
# print(type(winning_year))
# print(type(winning_prize))
# print(type(text_1))
# print(type(text_2))
# print(type(text_3))





'''
Write a pythone program where you will ask a user his/her full name and interviewID.
and then produce an output print statement as follow:

Hello "Full name", congratulation !!!
Your "InterviewID" indicates that you have been selected.
'''

# Name=input('What is your name?').strip().title()
# InterviewID=int(input('What is your interviewID?'))
# print("Hello",Name,",congratulation !!!", "Your",InterviewID ," indicates that you have been selected. ")

'''
Declare variable for the 2100 USD fare of Emirates and a tax rate of 2%. Then  print the following output 
"Emirates tickets are costing me sleepless nights because for ... USD, I could do a dental surgery in Dhaka"
'''

# fare_of_emirates=2100
# tax_rate=.02
# cost=fare_of_emirates+(fare_of_emirates*tax_rate)
#
# print("Emirates tickets are costing me sleepless nights because for", cost ,"USD, I could do a dental surgery in Dhaka.")



def scholarship(name,cgpa):
    print(f'My name is {name.strip().title()}.'
          f' My CGPA is {cgpa}')

scholarship('Shifat',3.97)