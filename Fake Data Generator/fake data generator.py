#!/usr/bin/env python
# coding: utf-8

# In[648]:


#!pip install faker
from faker import Faker
from datetime import date
fake = Faker() 


# In[649]:


#finalData
#finalData will be list of element (list of dictionerys(same as data_skeleton))
final_data = []

#noof data required
n = 1000
no_of_sensor_data = 1000


#other data
starting_data = date(2015, 1, 15)
end_date = date(2020, 12, 5)
days = end_date - starting_data
series = fake.time_series(start_date='-'+str(days.days + 1)+'d', end_date=str(int(no_of_sensor_data/4)-days.days)+'d', precision=int(6*60*60))
x = [val[0] for val in series]
dates = []
times = []
for i in x:
    dates.append(str(i.year)+"-"+str(i.month)+"-"+str(i.day))
    times.append(str(i.hour)+"-"+str(i.minute)+"-"+ str(i.second))


# In[650]:


#getting and storing the data in 
for i in range(n):
    
    #prepering sensor data
    sensor_data = []
    for j in range(no_of_sensor_data):
        OutsideTemperature = fake.random_int(70, 95)
        OutsideHumidity = fake.random_int(50, 95) 
        sensor_data_skeleton = {
            "Date":dates[j],
            "Time":times[j],
            "Outside Temperature":OutsideTemperature,
            "Outside Humidity":OutsideHumidity,
            "Room Temperature":OutsideTemperature - fake.random_int(0, 10),
            "Room Humidity":OutsideHumidity - fake.random_int(0, 10)
        }
        sensor_data.append(sensor_data_skeleton)
    
    #getting profile
    profile = fake.simple_profile()
    
    #storing for i th user
    data_skeleton = {
         "Firstname":str(profile["name"]).split(" ")[0],
         "Lastname": fake.last_name(), 
         "age":fake.random_int(0, 100),
         "gender": profile["sex"],
         "username": profile["username"],
         "address":profile["address"],
         "email": profile["mail"],
         "sensor_data" : sensor_data
    }
    
    final_data.append(data_skeleton)


# In[647]:


final_data

