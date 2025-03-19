Birth_Year=1996
Current_Year=2025
age=Current_Year-Birth_Year
print(age)

list=[2323,323,232]
lista2=[23]
var=2*2


my_name='Jhon jairo pabon gamas'
my_country='Colombia'
my_major='Enginner'
print(f' Old:{my_name}  New:{my_name.upper()}')
print(f' Old:{my_country}  New:{my_country.lower()}')
print(f' Old:{my_major}  New:{my_country.swapcase()}')

P=3
Q=1
D=2*(P+Q)
K=4*(P-Q)
print(f'P: {P}')
print(f'Q: {Q}')
print(f'D: {D}')
print(f'K: {K}')



####SEQUENCES


text='This is my 2nd Tutorial in MDS601'
lenText=len(text)
print(text)
print(f'length :{lenText}')
print(f' 6th value of the text variable: {text[6]}')
print(f'  last value of the text variable: {text[lenText-1]}')
updated_text=text.swapcase()
print(f'   Swap the case for the text variable: {updated_text}')


FName='jhon'
LName='pabon'
full_name=FName+' '+LName
print(full_name)


#LIST

my_list=[1,2.5,56,67,78,3]
my_list[0]=20
lenList=len(my_list)
firstTwoValues=my_list[0]+my_list[1]
my_list[lenList-1]=firstTwoValues
print(my_list)
valuesToExtend=[89,78]
my_list.extend(valuesToExtend)
print(my_list)
my_list.insert(3,-10)
print(my_list)
sorted_list = sorted(my_list)
print(f'sorted_list :{sorted_list}')
print(f'my_list :{my_list}')


#tuple

my_tuple=(1,2,3,4,5)
lenTuple=len(my_tuple)
print(f' length tuple: {lenTuple}')
print(f' last value tuple: {my_tuple[lenTuple-1]}')
my_tuple[2]=25 ##error ''tuple' object does not support item assignment' ,it can't because a tuple is not modifiable



#####Dictionary

my_data={'thais':32,'jhon':28,'johan':32,'maria':27,'juan':34}
print(my_data)
print(f' Student names: {my_data.keys()}')
print(f' Student Ages: {my_data.values()}')
print(f'johan age : {my_data["johan"]}')











