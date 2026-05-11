#c=()
#print(type(c))
c=(1,24,1,3,14,'kiran')
#print(c[-1])
#print(c[0:4:2])
c=(1,24,1,3,14)
print(min(c))
print(max(c))
print(sum(c))
print(len(c))
#concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
#repeate
c=(1,24,1,3,14,14)
print(c*11)
#iteration
for i in c:
    print(i)
#membership
print(1 in c)
print(11 not in c)
t1=(1,2,3)
t2=(4,5,6)
print(t1 is not t2)