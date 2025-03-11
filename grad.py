from bkgrad import grad

r1 = grad()

i=1 #initial
while(i<=3):
    print("subject marks")
    print("************")
    no1=int(input("enter the subject 1: "))
    no2=int(input("enter the subject 2: "))
    no3=int(input("enter the subject 3: "))


     
    r1.sum(no1,no2,no3)
    #print("average", r1.total/3)
    i=i+1
    question=input("do you want or not (y/n)")

    if(question=="n"):
        break  
        