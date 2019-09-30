class Zoo:
    name= "This is zoo."
    def __init__(self,zooname,keepername, maxno):
        print("Hi this is init function")
        self.zooname=zooname
        self.zookeeper=  keepername
        self.max= maxno
        self.animals= {}
    def addAnimal(self,aniname,anino):
        self.animals[aniname]=anino
            
    def removeAni(self,aniname):
        if aniname in self.animals:
           del self.animals[aniname]
        else:
            print('No such animal')
      
            
class bank:
    def __init__(self,bankname,acc_no,totalbalance, methoddep, methodwith):
        self.bankname= bankname
        self.acc_no= acc_no
        self.totalbalance=totalbalance
        self.methodwith=methodwith
        self.methoddep=methoddep

        
class market:
    def __init__(self,name,storehrs,employees,totalmoney,item1,price1,item2,price2,item3,price3):
        self.name= name
        self.storehrs=storehrs
        self.employees=employees
        self.totalmoney=totalmoney
        self.store={}
        self.item1= item1
        self.item2= item2
        self.item3= item3
        self.price1= price1
        self.price2= price2
        self.price3= price3
        self.store[item1]=price1
        self.store[item2]=price2
        self.store[item3]= price3
        self.purchased= {}
    def buy(self):
        print('Do you want to buy?')
        buyornot= input()
        while buyornot== 'Yes':
                    print('What do you want to buy?')
                    print(self.store)
                    purchase= input()
##                    if purchase in self.store:
##                        if len(purchased) <= 3:
##                            if purchase not in self.purchased:
                    if purchase== self.item1:
                        self.purchased[self.item1]= self.price1
                        print('Your cart is',self.purchased)
                        self.totalmoney= self.purchased.values()
                        print('Your bill is', self.purchased.values())
                        print('Do you want anything else?')
                        buyornot= input()
                    if purchase== self.item2:
                        self.purchased[self.item2]= self.price2
                        print('Your cart is',self.purchased)
                        self.totalmoney= self.purchased.values()
                        print('Your bill is', self.purchased.values())
                        print('Do you want anything else?')
                        buyornot= input()
                    if purchase== self.item3:
                        self.purchased[self.item3]= self.price3
                        print('Your cart is',self.purchased)
                        self.totalmoney= self.purchased.values()
                        print('Your bill is', self.purchased.values())
                        print('Do you want anything else?')
                        buyornot= input()
                    else:
                        print('item not in store')
                        print('Do you want anything else?')
                        buyornot= input()
                      
    def retur(self):
        
        print('Do you want to return anything?')
        retornot= input()
        while retornot == 'Yes':
            print('What do you want to return?')
            self.returning= input()
            if self.returning in self.purchased:
                if self.returning== 'Milk':
                    print('Milk cannot be returned')
                    print('Do you want to return anything else?')
                    retornot= input()
                else:
                    del self.purchased[self.returning]
                    print('Your item is returned. This is your cart', self.purchased)
                    self.totalmoney= self.purchased.values()
                    print('Your bill is', self.purchased.values())
                    print('Do you want to return anything else?')
                    retornot= input()
                    print('Item is returned')
            else:
                print('Item not found')

class phonebook:
    def __init__(self, book):
        self.book= {}
    def add(self):
        phone= True
        while phone== True:
            print('Whose phone number would you like to add?')
            adding= input()
            
            if adding not in self.book:
                print('What is their phone number?')
                number= input()
                if len(number)== 10:
                    self.book[adding]= number
                    print('Number added successfully')
                    print(self.book)
                    print('Would you like to add another number?')
                    numornot= input()
                    if numornot != 'Yes':
                        phone= False
                else:
                    print('Not a valid number')
                    print('Would you like to add another number?')
                    numornot= input()
                    if numornot != 'Yes':
                        phone= False
            else:
                print('Number already in phonebook')
                print('Would you like to add another number?')
                numornot= input()
                if numornot != 'Yes':
                    phone= False
    def remove(self):
        print('Would you like to remove a phone number?')
        removal1= input()
        print('Whose number would you like to remove?')
        removal2= input()
        if removal2 in self.book:
            print('Are you sure you want to remove?')
            removal3= input()
            if removal3== 'Yes':
                del self.book[removal2]
                print('Number removed. This is your book now', self.book)
                
            else:
                print('Number not in phonebook')
                
