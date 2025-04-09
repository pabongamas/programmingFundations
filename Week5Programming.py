## factorial code
def factorial(n):
    if(n==0):
        return 1
    else:
        return (n* (factorial(n-1)))

print('give the number to a factorial')
val=int(input())
variable=factorial(val)
print(variable)



## 2 point
def checkIsOddOEven(number):
    if(number%2==0):
        print("the number "+str(number)+" is even" )
    else:
        print("the number "+str(number)+" is odd" )

numValue=int(input("give me a number to know if its a odd or even number "))
checkIsOddOEven(numValue)

#3 PPOINT
def createMatrix(numberRows):
    for i in range(numberRows):
        numActual=i+1
        for j in range(numActual):
            print("*",end=" ")
        print("\r")


createMatrix(7)

## 4 point
def multipleOf5(lower,upper):
    values=range(lower,upper+1)
    listMultiples5=[]
    for i in values:
        if(i%5==0):
            listMultiples5.append(i)
    return listMultiples5

list=multipleOf5(30,70)
print(list)

#5 point


def swapLowerAndUpper(text):
    return text.swapcase()


text=input("text me something")
textChanged=swapLowerAndUpper(text)
print(textChanged)


#6 point


def maxValueInAList(listData):
    maxValue=0
    for value in listData:
        if(value>maxValue):
            maxValue=value
    return maxValue
maxValueReturned=maxValueInAList([5,6,8,91,2,5,85])

print(maxValueReturned)

# 7 point
def countWords(text):
    listWords=text.split()
    return len(listWords)


text=input("text me something")
count=countWords(text)
print(count)

