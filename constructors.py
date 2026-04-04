class person:
     def setvalue(self,name,age):
       self.name=name
       self.age=age
       def getvalue(self):
           print("the name of the person is",self.name,"and the age is",self.age,".",sep="")
           p=person()
           name=input()
           age=int(input())
           p.setvalue(name,age)
           p.getvalue()