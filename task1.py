
size=int(input( "enter size: "))
for r in range(0,size):
    for s in range(0,size-r):
        print(" ", end="")
    for c in range(0,r+1):
        print("*",end="")
    print("")
print("-------------------------------")



list=["a","e","i","o","u"]

for j in "mobile":
    if j not in list:
        print(j, end="")
print("")
print("------------------------------------------")
    
def letterposition(string, char):
    list=[]
    for i in range (len(string)):
        if string[i]==char:
            list.append(i)
    return list
print(letterposition("this is javascript","i"))

print("-----------------------------------------")
x= int(input("enter num"))
for i in range (1,x+1):
    multiplicatin=[]
    for j in range (1, i+1):
        multiplicatin.append(i*j)
    print ( multiplicatin)
print("--------------------------------------------")

import webbrowser
from random import choice
k=["http://www.google.com","https://realpython.com/python3-object-oriented-programing/"]
webbrowser.open(choice(k))
print("----------------------------------------------")

s1="Au{}lt"
s2="kelly"
print(s1.format(s2))
print("----------------------------------------------")

s1="yn"
s2="pynative"
if s1 in s2:
    print("true")

else:
    print("false")

a1="ynf"
a2="pynative"
if a1 in a2:
    print("true")

else:
    print("false")
print("--------------------------------------------------")

strr="apple"
s=list(strr)
print(s)


    
          
  
    
