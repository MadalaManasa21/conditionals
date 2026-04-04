a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
if a>b:
    if a>c:
        print("the greatest no is:",a)
    else:
        print("the greatet no is:",b)
else:
    if b>c:
        print("tne greatest no is:",b)
    else:
        print("the greatest no is:",c)
