L = ['a','b','c','d','e','f','g','h','i','j','k','l']
print(L[7:])
print(L[-7:-3])




#-----------Methods in lists-------------

Dates=[1,2,3,4,5,6,7,8,9]

#1. Append method- helps to adds eliments by the end of list

Dates.append('10')
print(Dates)  # this method adds eliments by the end of list

#2. pop metghods

Dates.pop()
print(Dates) # this method deletes an element by the end of list

#3. pop metghods to delete a particular element

Dates.pop(5)
print(Dates) # this method deletes perticular element according to index number


#4. insert method to add a particular element at a particular position

Dates.insert(5,55)
Dates.insert(6,565)

#5. remove method to delete a perticular element without indexing

Dates.remove(8)
print(Dates)

#6. remove method to delete a perticular element with indexing

del Dates[3]
print(Dates)