#!/usr/bin/env python
# coding: utf-8

# In[174]:


import pandas as pd
dta_at_hh=pd.read_csv('/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/dta_at_hh.csv')
dta_at_TC=pd.read_csv('/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/dta_at_TC.csv')


# In[182]:


# Part B-1
unique_hhid_in_trips=set(trips.hh_id)
print(len(unique_hhid_in_trips))


# In[183]:


hhid_groupby=trips.groupby(trips['hh_id']).size()
print(hhid_groupby)


# In[67]:


for row in trips:
    if trips


# In[59]:


unique_date=set(trips.TC_date)
print(len(unique_date))
print(sorted(unique_date))


# In[184]:


dta_at_TC.head()


# In[194]:


TC_date=dta_at_TC['TC_date']
print(TC_date)


# In[195]:


new_date=[]
for i in TC_date:
    new_date.append(i)


# In[196]:


new_date.pop(0)


# In[197]:


new_date.append('')


# In[198]:


len(new_date)


# In[199]:


len(dta_at_TC)


# In[200]:


dta_at_TC.drop([7596144])


# In[201]:


dta_at_TC['new_date']=new_date
dta_at_TC.tail()


# In[202]:


dta_at_TC['date_diff']=pd.to_datetime(dta_at_TC['new_date'])-pd.to_datetime(dta_at_TC['TC_date'])
dta_at_TC.head()


# In[203]:


import numpy as np
dta_at_TC['date_diff']=dta_at_TC['date_diff'].dt.days


# In[204]:


dta_at_TC.head()


# In[206]:


unique_id=set(dta_at_TC.hh_id)
print(len(unique_id))
unique_id=list(unique_id)
print(type(unique_id))
#print(unique_id)


# In[207]:


max_date_diff=dta_at_TC.groupby(dta_at_TC['hh_id']).max()


# In[128]:


print(type(max_date_diff))


# In[136]:


print(max_date_diff)


# In[130]:


print(type(dta_at_TC['date_diff']))


# In[208]:


date_diff_above_90=max_date_diff.loc[max_date_diff['date_diff']>90]


# In[209]:


household_id_list=date_diff_above_90['hh_id']
#print(set(household_id_list))
print(len(set(household_id_list)))


# In[ ]:





# In[210]:


# Part B-2
date_diff_below_30=max_date_diff.loc[max_date_diff['date_diff']<=30]
hhid_below_30_list=date_diff_below_30['hh_id']
print(len(set(hhid_below_30_list)))
#print(set(hhid_below_30_list))


# In[61]:


print(date_diff_below_30)


# In[19]:


grocery_expen=dta_at_TC.iloc[:,[1,3,6,9]]
grocery_expen.head()


# In[20]:


expenditure=grocery_expen['TC_total_spent'].groupby([grocery_expen['hh_id'],grocery_expen['TC_retailer_code']]).sum()
expenditure


# In[21]:


expen_cal=expenditure.unstack()


# In[22]:


expenditure_total=grocery_expen['TC_total_spent'].groupby(grocery_expen['hh_id']).sum()
expenditure_total


# In[23]:


above_80=expen_cal.div(expenditure_total, axis='rows')
print(above_80)


# In[35]:


above_80=pd.DataFrame(above_80)
above_80


# In[41]:


above_80.to_csv(r'/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/above_80.csv')


# In[45]:


above_80_new=pd.read_csv('/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/above_80.csv')


# In[50]:


above_80_new.head()


# In[91]:


#above_80_new.iloc[2].values[1]
above_80_new.iloc[[2],1]
above_80_new.iloc[[2],[1]]
#print(above_80_new.iloc[[2],[1]]>0)
above_80_new.iloc[[6],[2]]


# In[75]:


pd.DataFrame(expenditure)


# In[ ]:





# In[1]:


# Qb-2-1

import numpy as np
import matplotlib.pyplot as plt
# demographic - race
n_groups_1=3
single_retailer=(866, 45, 12)
two_retailers=(3257, 193, 51)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_1)
bar_width=0.35
opacity=0.8

race=plt.bar(index, single_retailer, bar_width, alpha=opacity, color='pink', label='Single Retailer')
race2=plt.bar(index+bar_width, two_retailers, bar_width, alpha=opacity, label='Two Retailers')


plt.ylabel('Distribution')
plt.title('Race')
plt.xticks(index+bar_width, ('White Caucasian','African American','Asian'))
plt.legend()

plt.show()


# In[115]:


# Latino
n_groups_2=2
single_retailer=(45,926)
two_retailers=(3257,3502)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_2)
bar_width=0.35
opacity=0.8

race=plt.bar(index, single_retailer, bar_width, alpha=opacity, color='pink', label='Single Retailer')
race2=plt.bar(index+bar_width, two_retailers, bar_width, alpha=opacity, label='Two Retailers')


plt.ylabel('Distribution')
plt.title('Latino')
plt.xticks(index+bar_width, ('Yes','No'))
plt.legend()

plt.show()


# In[120]:


# Income
n_groups_2=16
single_retailer=(10,23,20,31,44,70,83,78,79,59,74,59,108,65,112,56)
two_retailers=(39,84,62,97,161,268,364,304,300,257,257,226,393,252,409,224)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_2)
bar_width=0.35
opacity=0.8

race=plt.bar(index, single_retailer, bar_width, alpha=opacity, color='pink', label='Single Retailer')
race2=plt.bar(index+bar_width, two_retailers, bar_width, alpha=opacity, label='Two Retailers')


plt.ylabel('Distribution')
plt.title('Income')
plt.xticks(index+bar_width, (3,4,6,8,10,11,13,15,16,17,18,19,21,23,26,27))
plt.legend()

plt.show()


# In[117]:


# Household Size
n_groups_3=9
single_retailer=(278,292,152,143,71,28,5,2,0)
two_retailers=(1024,1187,566,546,243,99,22,7,3)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_3)
bar_width=0.35
opacity=0.8

race=plt.bar(index, single_retailer, bar_width, alpha=opacity, color='pink', label='Single Retailer')
race2=plt.bar(index+bar_width, two_retailers, bar_width, alpha=opacity, label='Two Retailers')


plt.ylabel('Distribution')
plt.title('Household Size')
plt.xticks(index+bar_width, (1,2,3,4,5,6,7,8,9))
plt.legend()

plt.show()


# In[118]:


# Residence
n_groups_4=8
single_retailer=(686,20,38,0,99,30,98,0)
two_retailers=(2732,45,148,4,341,118,309,0)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_4)
bar_width=0.35
opacity=0.8

race=plt.bar(index, single_retailer, bar_width, alpha=opacity, color='pink', label='Single Retailer')
race2=plt.bar(index+bar_width, two_retailers, bar_width, alpha=opacity, label='Two Retailers')


plt.ylabel('Distribution')
plt.title('Residence Type')
plt.xticks(index+bar_width, (1,2,3,4,5,6,7,8))
plt.legend()

plt.show()


# In[121]:


# Qb-2-3
dta_at_hh=pd.read_csv('/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/dta_at_hh.csv')


# In[122]:


dta_at_hh.head()


# In[124]:


state_type=set(dta_at_hh.hh_state)
print(state_type)
print(len(state_type))


# In[ ]:





# In[153]:


# Part B-3-3
dta_at_TC.head()


# In[154]:


dta_at_TC_new=dta_at_TC[dta_at_TC['date_diff']>=0]


# In[155]:


dta_at_TC_new.head()


# In[157]:


consecutive_date_count=dta_at_TC_new['date_diff'].groupby(dta_at_TC_new['hh_id']).count()
consecutive_date_count


# In[158]:


consecutive_date_sum=dta_at_TC_new['date_diff'].groupby(dta_at_TC_new['hh_id']).sum()
consecutive_date_sum


# In[161]:


consecutive_date=pd.merge(consecutive_date_sum, consecutive_date_count)
consecutive_date


# In[162]:


consecutive_date=consecutive_date_sum.div(consecutive_date_count, axis='rows')
print(consecutive_date)


# In[169]:


consecutive_date.to_csv(r'/Users/raphael/Desktop/Brandeis/Academic/Course/2019 Fall/BUS-211F Analyzing Big Data I/Final/consectuive_date.csv')


# In[3]:


# Consecutive Date
n_groups_5=6
date=(16386, 16913, 4302, 1315, 399, 262)

fig, ax=plt.subplots()
plt.figure(figsize=(10,10))
index = np.arange(n_groups_5)
bar_width=0.35
opacity=0.8

race=plt.bar(index, date, bar_width, alpha=opacity)


plt.ylabel('Distribution')
plt.title('Average Consecutive Date')
plt.xticks(index+bar_width, ('<=2','<=4','<=6','<=8','<=10','>10'))
plt.legend()

plt.show()

