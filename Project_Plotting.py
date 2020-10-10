#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:44:22 2019

@author: yimingxiong
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Health & Beauty Care','General Merchandise',
'Non-Food Grocery'   	
'Dry Grocery	',	  
'Frozen Foods',		  
'Fresh Produce',
'Dairy',	  
'Packaged Meat',  
'Deli',		  
'Alcoholic Beverages	',
'Magnet Data',		  
'Null')
y_pos = np.arange(len(objects))

performance = [180, 194, 141, 445, 90, 27,48, 15,18,33,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=90)
plt.ylabel('Module Number')
plt.title('Department')
plt.show()
objects = ('Health & Beauty Care','General Merchandise','Non-Food Grocery', 'Dry Grocery','Frozen Foods','Fresh Produce','Dairy','Packaged Meat', 'Deli', 'Alcoholic Beverages',
            'Null')
y_pos= np.arange(len(objects))
performance = [169236, 151670, 152747, 397527, 63623, 10250, 42434, 15851, 34623, 2600, 3620]


plt.bar(y_pos, performance,align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=90)
plt.ylabel('Department')
plt.title('Private Label')
plt.show()


""""Average number of items""""
objects =('Dec','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec')
y_pos = np.arange(len(objects))

performance = [326854,2461658,2314282,2408332,2469202,2412117,2218160,2331443,2407177,2250080,2439804,2380645,2000264]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=90)
plt.title('Average number of items')
plt.show()


""""Trips per MonthTrips per MonthTrips per Month"""
objects =('Dec','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec')
y_pos = np.arange(len(objects))

performance = [225127,1676425,1580509,1646288,1617844,1651182,1526356,1587560,1632725,1527362,1657190,1604588,1360815]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos,objects,rotation=90)
plt.xlabel("2003/12-2004/12", color="r")
plt.title('Trips per Month ')
plt.show()


x =('Dec','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec')
y_pos= np.arange(len(objects))

y= [1.4519,1.4684,1.4643,1.4629,1.4644,1.4608,1.4532,1.4686,1.4743,1.4732,1.4723,1.4836,1.4699]
plt.bar(x, y, align='center', alpha=0.5)
plt.xticks(y_pos,objects,rotation=90)
plt.xlabel("2003/12-2004/12", color="b")
plt.yticks(np.arange(0,1.5))
plt.title('Average number of items purchaced per Month')
plt.show()
####product per department ####

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
plt.bar(align="center", alpha=0.5)

x =('Dec','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec')
y= [1.4519,1.4684,1.4643,1.4629,1.4644,1.4608,1.4532,1.4686,1.4743,1.4732,1.4723,1.4836,1.4699]
colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Items Purchaced per Months')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# Create data
y=[1.4519,1.4684,1.4643,1.4629,1.4644,1.4608,1.4532,1.4686,1.4743,1.4732,1.4723,1.4836,1.4699]
x= [225127,1676425,1580509,1646288,1617844,1651182,1526356,1587560,1632725,1527362,1657190,1604588,1360815]
colors = (0,0,0)
area = np.pi*4
np.corrcoef(x, y)
# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.xlabel('Shopping Trips')
plt.ylabel('Items per trip')
plt.show()

######## Question 2 
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Dec','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec')
y_pos= np.arange(len(objects))
performance = [0.03979307498652565,0.039536659129414765,0.03908689711594724,0.040172340846733275,0.040452691662570206,0.039649647129591466,0.03805495995896507,0.039340231845669586,0.036651458559342036,0.0395079901004285,0.03983761694144599,0.03840381172049345,0.03921476727539835]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=90)
plt.title('Precentage of Private Label Product in Total Purchased')
plt.show()
####product per department ####


