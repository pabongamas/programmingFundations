# import numpy as np
# array=np.array([1,8,2,5,0,2,4,7,2])

# # operation on this array. 
# # a. Print the array. 
# print(array)
# # b. Sort the array and print the sorted array. 
# sorted=np.sort(array)
# print(sorted)
# # c. Find the sum of all values of the array. 
# sum=np.sum(array)
# print(sum)
# # d. Find the average of all the values of the array. 
# average=np.average(array)
# print(average)
# # e. Find the maximum and minimum values of the array. 
# maxValue=np.max(array)
# minValue=np.min(array)
# print(f'The maximun is {maxValue} and the minimun is {minValue}')


# # Write a Python program to plot the Maximum and Minimum temperature against all the 
# # months. Provide all the necessary information for your graph. 
# Max_Temp = [32,30,31,28,29,25,22,18,19,22,25,28] 
# Min_Temp = [28,26,25,23,24,20,18,13,14,16,18,22] 
# Months = ['Jan','Feb','Mar','Apr','May','Ju','Jul','Aug','Sep','Oct','Nov','Dec'] 

# import matplotlib.pyplot as plt
 
# plt.plot(Months,Max_Temp,color='blue')
# plt.plot(Months,Min_Temp,color='red')

# plt.xlabel("Months")
# plt.ylabel("Temperature")
# plt.show()

# # Write a Python function that takes some string (for example, “I need to write THIS 
# # sentence to a TEXT file using PYTHON”) as input and writes it to a file. Name the file as 
# # your name.txt


# stringText="I need to write THIS sentence to a TEXT file using PYTHON"
# file=open('C:/Users/JhonJairoPABONGAMAS/Desktop/Programming foundations/textTest.txt',mode='r')
# for value in file:
#     print(value)

# fileToWrite=open('C:/Users/JhonJairoPABONGAMAS/Desktop/Programming foundations/textTest.txt',mode='w')
# fileToWrite.write(stringText)
# fileToWrite.close()


# Write a Python function that reads the content of a file created in Question 3 and finds 
# all the upper-case words. Add these uppercase words to a list and then print the list. 

# lettersUpper=[]
# file=open('C:/Users/JhonJairoPABONGAMAS/Desktop/Programming foundations/textTest.txt',mode='r')
# for line in file: 
#     words = line.split() 
#     for word in words:
#         if word.isupper():
#             lettersUpper.append(word)

# print(lettersUpper)

# Using Python, create a class named pet with attributes name and gender. Using the 
# constructor, set the values of these attributes. Define a method named display() that 
# prints the name and gender of the pet. Create two objects for the pet class; one object 
# for a dog and one for a cat. Provide appropriate values to the attributes.

# class Pet:
#     name=""
#     gender=""
#     def __init__(self,nameParam,genderParam):
#         self.name=nameParam
#         self.gender=genderParam
    
#     def display(self):
#         print(f'Name:{self.name} and Gender:{self.gender}')


# pet1=Pet("DOG","Male")
# pet2=Pet("CAT","Female")
# pet1.display()
# pet2.display()



# Using Python, create a class named Order with attributes product_mount and price. Using 
# the constructor, set the values of these attributes. Define a method named calculate_bill() 
# that returns the total bill for the Order (product_amount*price). Create two objects for 
# the order class and provide appropriate values to the attributes. Print the total bill for 
# both objects.

class Order:
    product_mount=0
    price=0
    def __init__(self,productMountParam,priceParam):
        self.product_mount=productMountParam
        self.price=priceParam
        
    def calculateBill(self):
        return self.product_mount*self.price
    
order1=Order(3,1500)
order2=Order(6,2500)
bill1=order1.calculateBill()
bill2=order2.calculateBill()
print(f'The total bill for order 1  is {bill1} and for order 2 is {bill2}')