# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:55:01 2022

@author: umamah
"""

import numpy as np
import matplotlib.pyplot as plt       #library files required for coding project
from scipy import stats  

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = np.loadtxt("C:/Users/samkh/Desktop/fds1 assignment/inputdata6.csv",
                 delimiter=",", dtype=str) #delimiter used to give the gap between columns by a comma and dtype is used to tell the type of the data
display(data)

data = np.delete(data, (0), axis=0)#dropped first row as they were not required for plotting a scatter plot and string will create mess
display(data)
print(type(data))
print(data[0][1])#to see whether the array is correctly printing the data using indices

#plot a two dimensional scatter plot

plt.figure(figsize=(10,10))

plt.scatter(data[:,0],data[:,1]) # used plt.scatter function to plot a scatter plot as a two-dimensional array
plt.title('scatter plot of Data')#gives title
plt.xlabel('Rainfall Precipitation')#label x axis
plt.ylabel('Productivity Coefficient')#labeling y axis
plt.xticks(rotation=50)#adjustement of the values on x axis
plt.show()

my_x = data[:,0].reshape(-1,1)#spliting data to x and y variables
my_x = my_x.astype(float)
my_y = data[:,1]
my_y = my_y.astype(float)
X_Train, X_Test, Y_Train, Y_Test = train_test_split(my_x, my_y, test_size=1/3,
                                                    random_state=0) # nitializing the variables for the model

model = LinearRegression()#calling linear regression to fit it on the split data
model.fit(X_Train, Y_Train)#fit function fits the trained data on the model

r_sq = model.score(my_x, my_y)
print(f"coefficient of determination: {r_sq}")#checking coefficient of determination

# Predicting the Test set result ￼
Y_Pred = model.predict(X_Test).reshape(-1,1)
print(Y_Pred)

print(f"intercept: {model.intercept_}")#just printing the intercept of the model to test the correct fitness of the model
intercept: 5.633333333333329

print(f"slope: {model.coef_}")#testing slope to see the correct fit of the model
slope: [0.54]
    
plt.scatter(X_Train, Y_Train, color='green')#plots trained data on same one plot
plt.scatter(X_Test, Y_Test, color='red')#plots test data with different color but in a same plot
plt.plot(X_Train, model.predict(X_Train), color='blue')#plots the regression line
plt.title('Rainfall vs Productivity  (Test Set=red)(Train set=green)')
plt.xlabel('Rainfall')
plt.ylabel('Productivity')
plt.show()

#predicted value for studentid ending at 6=245.0
x_in_mm = 245.0
predicted_x = np.array([x_in_mm]).reshape(-1,1) # reshaping to avoid arraysize index error
predicted_x = predicted_x.astype('float')
predicted_y = model.predict(predicted_x)
predicted_y = predicted_y.astype('float')

plt.scatter(X_Train, Y_Train, color='green')#plotting training set
plt.scatter(X_Test, Y_Test, color='red')#plotting testing set
plt.plot(X_Train, model.predict(X_Train), color='black')#plotting regression line
plt.plot(predicted_x,predicted_y,c='b',marker='*',markersize=20)#plotting the predicting value
plt.title('graph for predicted value for X(mm)=245.0')
plt.xlabel('Rainfall')
plt.ylabel('Productivity')
plt.show()