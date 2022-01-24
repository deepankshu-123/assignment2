#question 1
string1 = "Python is a case sensitive language"
#a
print(len(string1))
#b
print(string1[::-1])
#c
print(string1[10:26])
#d
print(string1.replace("a case sensitive","object oriented"))
#e
print(string1.find("a"))
#f
print(string1.replace(" ",""))


#question 2
name= "deepankshu gautam"
SID=21104013
department="electrical"
cgpa=9.9
print("Hey,",name,"Here!")
print("My SID is",SID)
print("I am from",department,"department and my CGPA is",cgpa)


#Question 3
a=56
b=10
#a
print(a&b)
#b
print(a|b)
#c
print(a^b)
#d
print(a<<2,b<<2)
#e
print(a>>2,b>>4)


#question 4
number1=int(input("Enter the first number "))
number2=int(input("Enter the second number "))
number3=int(input("Enter the third number "))
list=[number1,number2,number3]
print("The greatest of the three numbers entered is: ",max(list))


#question 5
string2=input("Please Enter the text in which you want to check presence of 'name'\n")
if "name" in string2:
    print("Yes")
else:print("No")


#question 6
len1=int(input("Enter the first side"))
len2=int(input("Enter the second side"))
len3=int(input("Enter the third side"))
print("Can these sides form a triangle?")
if len1>=len2+len3:
    print("No")
elif len2>=len1+len3:
    print("No")
elif len3>=len2+len1:
    print("No, triangle can't be formed!")
else:print("Yes, triangle can be formed!")
