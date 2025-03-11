class calculator:
    def sum(self,num1,operator,num2):
        no1=num1
        operator=operator
        no2=num2
       
        if(operator=="+"):

            total=no1+no2
            return total
        elif(operator=="-"):
            total=no1-no2
            return total

r1 = calculator()
while(True):
    print("time")
    print()
    n1=int(input("n1"))
    operator = input()
    n2=int(input("n1"))
    print("total", r1.sum(n1,operator,n2))

