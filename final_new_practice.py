import matplotlib.pyplot as plt
import pandas as pd

office_supplies=pd.read_csv('CSV File - Euro Debt Crisis.csv')
print('This is data of office supplies \n',office_supplies)

office_supplies=office_supplies.sort_values(['Amount'], ascending = True)
office_supplies.to_csv('modified_new')

office_supplies_Amount=[20,30,40,50,60]
office_supplies_Debtor=['Greece_1','United States','Greece_1','Greece_1','Portugal']
take_out=[0.2,0,0,0,0]


plt.style.use('ggplot')
plt.title('This is supplies list')
plt.pie(x=office_supplies_Amount,labels=office_supplies_Debtor,autopct='%.2f%%',
        shadow=True, startangle=50, explode=take_out)

plt.axis=('equal')
plt.legend(loc='upper left')

donut=plt.Circle(xy=(0,0),facecolor='white',radius=.5)
plt.gca().add_artist(donut)
plt.show()
