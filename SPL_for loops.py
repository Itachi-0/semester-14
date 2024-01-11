#-----------for loops----------

'''
I is Itiration
'''

# for i in range(6):    #last value hocche limit and eta print hobena.
#     print(i)
#
# for i in range(1,6):  #This will print from 1-5
#     print(i)


# for i in range(1,21,2):  # this will print 1 to 19, last position will not print
#     print(i)

# for i in range(0,20,2):
#     print(i)


'''
Sum all number from 1-100
'''
result=0
for i in range(1,101):
    result=result+i
print(result)

'''
Sum all odd number from 1-100
'''
Odd_result=0
for i in range(1,101,2):
    Odd_result=Odd_result+i
print(Odd_result)

'''
Sum all even number from 1-100
'''
E_result=0
for i in range(0,101,2):
    E_result=E_result+i
print(E_result)