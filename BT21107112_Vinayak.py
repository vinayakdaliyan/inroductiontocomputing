Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#QUESTION 1

String=str(input("Enter the string :"))


print("The length of given string is : ",len(String))

print("The reverse of string is:",String[::-1])

# SLICE OPERATION
new_string=String[10:26:1]
print('new string using slice operation :',new_string)


# REPLACING SUBSTRING

replacing=String.replace("a case sensitive","object oriented")    # replacing
print(replacing)


# INDEXING OF SUBSTRING

print("indexes of a are :",String.index("a",0,11),String.index("a",11,16),String.index("a",16,35))

# REMOVE WHITE OR BLANK SPACES
print("string after replacing blank spaces :",String.replace(" ",""))


#QUESTION 2
Name="VINAYAK"
SID=21107112
CGPA=9.9
Department="Mechanical"

print("Hey",Name,"Here!")
print("My SID is",SID)
print("Iam from",Department,"department and my cgpa is:",CGPA)





#QUESTION 3

a=56       
b=10


print("A. a & b =", a & b)

# Use of Bitwise OR(|) operator.
print("B. a | b =", a | b)

# Use of Bitwise XOR(^) operator.
print("C. a ^ b =", a ^ b)

# Use of shift(left) operator.
print("D. a << 2 = ", a << 2)

# Use of shift(both) operator.
print("E. a >> 2 = ", a >> 2, " and ", "b >> 4 = ", b >> 4)





#QUESTION 4

string=str(input("Enter a string :"))

if "name" in string:
    print("yes")
else:
    print("no")

    


#QUESTION 6

def function(a,b):
    ab_xor=a^b
    count=0
    while ab_xor:

        count=count+ (ab_xor & 1)
        ab_xor=ab_xor>>1
    print(count)


a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
function(a,b)





#QUESTION 5
      
# Taking inputs of the sides of the triangle.
n1 = int(input("Enter First length : "))
n2 = int(input("Enter Second length : "))
n3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
F1 = n1 > n2 + n3
F2 = n2 > n1 + n3
F3 = n3 > n1 + n2

# Here we check wheather the all conditions are satisfied or not.
Output = str(F1 or F2 or F3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))