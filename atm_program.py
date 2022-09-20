
#atm simple prog.
user_name=input("enter user name: ")
pass_word=input("enter password: ")
username='suneel'
password='1234'

if user_name==username and pass_word==password:
    print("log in successfull")
    amount=1000
    print("press 1 to credit")
    print("press 2 to debit")
    print("press 3 to ministatement")
    n=input("select the number 1 or 2 or 3: ")
    if (n=='1'):
        credit=int(input("enter the amount: "))
        amount=amount+credit
        print(amount)
    elif(n=='2'):
        debit=int(input("enter the debit amount: "))
        if amount>debit:
           amount=amount-debit
           print(amount)
        else:
            print("insufficiant amount")
    if (n=='3'):
        m=amount
        print(m)
    else:
        print("not available")
else:
    print("wrong password")   
    
    



