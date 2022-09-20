
from datetime import datetime



user_name=str(input('Enter user name: '))
password=int(input('Enter password: '))

User_name='suneel'
Password=1234
if user_name==User_name and password==Password:
    name=input("enter name:  ")
    mobile_no=input("mobile no: ")
#list
list='''
 #rooms
 'single bed'=1500 
 'double bed'=3000
 'extra bed'=900
 #food
 'tiffen items'=400
 'lunch itmes'=600
 'dinner'=600
 #failities
 'wifi'=100
 'pool'=150
 'drinks'=500
'''
#

rooms={'single bed':1500,
       'double bed':3000}
foods={'tiffen':400,
       'lunch':600,
       'dinner':600}
fecilities={'wifi':100,
            'pool':150,
            'drinks':500,
            'extra bed':900}
serviceslist=[rooms,foods,fecilities]

#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

option=int(input('for list of services press1'))
if option==1:
    print(list)   
for i in serviceslist:
    print("press 1 rooms")
    print("press 2 food")
    print("press 3 fecilities")
    inp1=int(input("select 1 or 2 or 3: "))
    if inp1==1:
        room=input('Enter your rooms: ')
        quantity=int(input('Enter your quantity: '))
        if room in rooms.keys():
            price=quantity*(rooms[room])
            print(price)
            if inp1==2:
                food=input('Enter your food: ')
                quantity=int(input('Enter your quantity: '))
                if food in foods.keys():
                    price=quantity*(foods[food])
                    print(price)       
                    if inp1==3:
                        fecilitie=input('Enter your fecilities: ')
                        quantity=int(input('Enter your quantity: '))
                        if fecilitie in fecilities.keys():
                            price=quantity*(fecilities[fecilitie])
                            print(price)
                            print(price)
                        else:
                            print('error')
                    else:
                        print('error2')
                else:
                    print('some thing wrong')
            else:
                    print('some thing wrong')
        else:
                    print('some thing wrong')
    else:
        print('else')
    inp=(input("can you want bill yes or no:"))
    if inp=='yes':
        pricelist.append((rooms,foods,fecilities,quantity))
        totalprice+=price
        ilist.append(rooms.items())
        ilist.append(foods)
        ilist.append(fecilities)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalprice*5)/100
        finalprice=gst+totalprice
        pass
        if finalprice!=0:
            print(25*"=","hotel management",25*"=")
            print(28*" ","tirupati")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            

            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],16*' ',qlist[i],18*" ",plist[i])
                print(75*"-")
                print(50*" ",'totalamount:','Rs',totalprice)
                print("gst amount",40*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalamount:','Rs',finalprice)
                print(75*"-")
                print(20*" ","Thanks for visiting")
                print(75*"-")
        
    
   
         

        
             
             

       
    