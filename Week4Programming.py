# x=4
# while x>0:
#     print('x is positive')
# print('Exited the loop as x is no longer positive ')


# x=4
# while x>0:
#     print('X is positive')
#     x=x-1
# print('exited the loop as x is not longer positive')


# text='welcome'
# p=0
# while p<len(text):
#     print(text[p])
#     p=p+1
    

# p=[2,4,6,8,10]
# for v in p:
#     print(v)
# num1=(int)(input())
# print("number 1 is",num1)
# num2=(int)(input())
# print("number 2 is",num2)
# num3=(int)(input())
# print("number 3 is",num3)

# if(num1>num2):
#     if(num1>num3):
#         print('Highest value is',num1)
#     else:
#         print('Highest value is',num3)
# elif(num2>num3):
#     print('Highest value is',num2)
# else:
#     print('Highest value is',num3)
    
    
# Write a program (using loops) to print the following pattern. 
# 1 1 1 1 1 1  
# 2 2 2 2 2 2  
# 3 3 3 3 3 3  
# 4 4 4 4 4 4  
# 5 5 5 5 5 5 

for variableI in range(5):
    valActualI=variableI+1
    for variableJ in range(5):
        print(valActualI,end='')
    print("\r")
    
print("***********************")  
# for variableI in range(5):
#     valActualI=variableI+1
#     for variableJ in range(valActualI):
#         print(valActualI,end='')
#     print("\r")
    
# Write a program to generate and print 10 random numbers between 20 and 50. Find 
# and print all the even numbers from these randomly generated numbers.     
import random
listRandomNumbers=[]
for variable in range(10):
    numberRandom=random.randrange(20,50)
    listRandomNumbers.append(numberRandom)
print(listRandomNumbers)

listPrimes=[]
for variable in range(20,50):
    flag=0
    for j in range(2,variable):
        if variable%j==0:
            flag=1
        
            


for variableI in range(5):
    valActualI=variableI+1
    for variableJ in range(5):
        print("*",end='')
    print("\r")
    
for variable in range(5):
    print((variable+1)*"*")
print("\r")