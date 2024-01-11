import pandas as pd

# importing a csv file

office_supplies= pd.read_csv("CSV File - Office Supplies.csv")
print('This following data is from office suppliers \n',office_supplies)


office_supplies = office_supplies.sort_values(['Unit Price'], ascending=False)
office_supplies.to_csv('Modified_office_supplies_file')

import matplotlib.pyplot as plt
# lets create a pie chart
office_supplies_price = [275, 125, 125, 23.95, 19.99]
office_supplies_Item_labels = ['Desk1', 'Desk2', 'Desk3', 'Pen Set', 'Pen']


plt.style.use('ggplot')
plt.title('office supplies')
takeout = (0.1, 0, 0, 0, 0)

plt.pie(x=office_supplies_price, labels=office_supplies_Item_labels, autopct='%2f%%',
        shadow=True, startangle=90, explode=takeout)
plt.axis('equal') #It means provide equal aspect ratio, which will draw the pie chart in a equally devided circle
plt.legend(loc='upper left')

plt.show()


'''
what is autopct in python?
Autopct is a parameter that allows us to display the percent value using string formatting

'''


# lets create a pie chart
office_supplies_price = [275, 125, 125, 23.95, 19.99]
office_supplies_Item_labels = ['Desk1', 'Desk2', 'Desk3', 'Pen Set', 'Pen']


plt.style.use('seaborn-v0_8-paper')
plt.title('office supplies')
takeout = (0.1, 0, 0, 0, 0)

plt.pie(x=office_supplies_price, labels=office_supplies_Item_labels, autopct='%0.2f%%',
        shadow=True, startangle=90, explode=takeout)
plt.axis('equal') #It means provide equal aspect ratio, which will draw the pie chart in a equally devided circle
plt.legend(loc='upper left')
donut = plt.Circle(xy=(0, 0), radius=0.4, facecolor='white')
plt.gca().add_artist(donut)
plt.show()
