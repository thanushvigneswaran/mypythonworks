class RealTimeInput:
    def sum(self,num1,operator,num2):

        no1=num1
        operator=operator
        no2=num2
       
        if(operator=="+"):

            total = no1+no2
            return total
        elif(operator=="-"):
            total = no1-no2
            return total

r1 = RealTimeInput()

i=1
while(i<=3):
    print("time")
    print("************")
    n1=int(input("enter the n1"))
    operator = input("please input the operator")
    n2=int(input("enter the n2"))
    print("total", r1.sum(n1,operator,n2))
    print()
    i=i+1
    question=input("do you want or not (y/n)")

    if(question=="n"):
        break  
    