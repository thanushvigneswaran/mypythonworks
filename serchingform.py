
i=1 #initial
while(i<=3):

    print("nformation personals")
    print("************")
    name=input("enter the name : ")
    fname=(input("enter the fname : "))
    age=(input("enter the age : "))
    dateofbirth=(input("enter the dateofbirth : "))
    address=(input("enter the address : "))
    telno=(input("enter the telno : "))
    emailaddress=(input("enter the emailaddress : "))

    #age, dateofbirth, address,telno,emailaddress 
    
    print()

    print("information personal")
    print("************")

    print("name:", name)
    print("fname:", fname)
    print("age", age)
    print("dateofbirth", dateofbirth)
    print("address", address)
    print("telno", telno)
    print("emailaddress", emailaddress)
     
    
    i=i+1
    question=input("do you want or not (y/n)")

    if(question=="n"):
        break  