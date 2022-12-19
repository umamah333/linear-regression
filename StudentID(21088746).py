# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:14:11 2022

@author: umamah
"""

import numpy as np                  #library file to be used for using different functions and printing 
                                   #csv file as an array
import matplotlib.pyplot as plt   #importing matplot libraries to plot graphs
from scipy import stats           #for implementing and making linear regression model 
                                      #this library package was required

# Question:01     read the data into Python numpy array(s), (0-4 points)
# using loadtxt()
arr = np.loadtxt("C:/Users/samkh/Desktop/fds1 assignment/inputdata6.csv",
                 delimiter=",", dtype=str) #delimiter used to give the gap between columns by a comma and dtype is used to tell the type of the data
display(arr) # used to display the data in the form of an array

arr = np.delete(arr, (0), axis=0)#dropped first row as they were not required for plotting a scatter plot and string will create mess
display(arr)

#Question:02.......plot the data as a two-dimensional scatter plot, (0-5 points)
# independant variable which is rainfall in this case will be plotted on x-axis and dependant variable productivity will be plotted on y-axis

plt.figure(figsize=(7,5))
plt.scatter(arr[:,0],arr[:,1]) # used plt.scatter function to plot a scatter plot as a two-dimensional array
plt.title('2D scatter plot of Data')#title for the plot
plt.xlabel('Amount of Rainfall Precipitation')#used to label x axis
plt.ylabel('Productivity Coefficient')#labeling y axis
plt.xticks(rotation=60)#for adjusting the values on x axis
plt.show()

rainfall_x = arr[:,0]#dividing 2D array into x and y variables for implementing linear regression.
rainfall_x = rainfall_x .astype(float) #converted datatype into float because mathematical operations cannot be performed
                                       #with reduced flexible type.so type casting was done explicitly

productivity_y = arr[:,1] 
productivity_y = productivity_y.astype(float)
display(rainfall_x,productivity_y) #displaying to check 

#Question:03.....create a linear regression model based on the data, and (0-7points)
#Question:04...... plot the corresponding line over the original data. (0-5 points)
#The resulting graphs should have adequate axis labels (0-2 points).

slope, intercept, r, p, std_err = stats.linregress(rainfall_x,productivity_y)#initializing the variables for linear regression model

def myfunc(rainfall_x):#function definition
    ''' a function that uses the slope and intercept values to return a new value. 
    This new value represents where on the y-axis the corresponding x value will be placed:''' #docstring explaining function's role
    return slope * rainfall_x + intercept #formula of linear regression


mymodel = list(map(myfunc, rainfall_x))#function call with mapping the arrays in the form of list to run in the form of loop for using each value of array

plt.scatter(rainfall_x,productivity_y,c='g',label='Scatter Plot')#prints scatter dots displaying the values of X and Y arrays 
plt.plot(rainfall_x, mymodel,color = 'black', linewidth=3, label = 'Regression Line')#prints regression line to display the linear regression model
plt.title('Linear Regression model of the given data')#prints title of the graph
plt.xlabel('Amount of Rainfall Precipitation')#prints x-axis label
plt.ylabel('Productivity Coefficient')#prints y-axis label
plt.show()
print(r)#view the correlation betwwen the x and y variables


#Question (5 points)
#Based on the linear regression model, evaluate the productivity co-
#efficient of the field if the amount of precipitations is X mm. The re-
#sulting value (predicted productivity coefficient) needs to be printed
#on the plot.
#IMPORTANT: You must predict the productivity coef-
#ficient for value X given in the table below.
#Last digit of your ID File name Value X
#STUDENT ID:21088746,last digit === 6  inputdata6.csv valu==245.0



slope, intercept, r, p, std_err = stats.linregress(rainfall_x,productivity_y)#the same model is used to plot the predicted value

def myfunc(rainfall_x):
    ''' a function that uses the slope and intercept values to return a new value. 
    This new value represents where on the y-axis the corresponding x value will be placed:'''
    return slope * rainfall_x + intercept #will calculate and return the values 

Xmm = 245.0
amount_of_precipitation = myfunc(Xmm)#the precipittion amount in mm is passed as an argument to the linear regression model

print('predicted productivity coefficient is=',amount_of_precipitation)#prints the resulting value

mymodel = list(map(myfunc, rainfall_x))#calling the linear regressed function to plot

plt.scatter(rainfall_x,productivity_y,c='r',label='Scatter Plot')#this will produce the values of X and Y of the input data
plt.plot(Xmm,amount_of_precipitation,c='b',marker=".", markersize=20)#the value 245.0 was sent to model to predict the output for y,so it will plot that value on plot with color 'blue' indicating the rainfall Xmm=245.0 
plt.plot(rainfall_x, mymodel,color = 'black', linewidth=1, label = 'Regression Line')#prints regression line  
plt.title('displaying the productivity coefficient for value X=245.0')#displays the title of the graph
plt.xlabel('Amount of Rainfall Precipitation')#prints x-axis label
plt.ylabel('Productivity Coefficient')#prints y-axis label
plt.show()
