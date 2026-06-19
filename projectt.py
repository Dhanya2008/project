print("City Central Library")

#Constructor
class Data:
    def __init__(self):
        name=input("Enter your name: ")
        phno=int(input("Enter your phone number: "))
        self.name=name
        self.phno=phno
    def display(self):
            print("Welcome to our library,",self.name)
            print("Let you curiosity lead the way !!")
d1=Data()
d1.display()


#Single inheritance

class Books:
    def preference(self):
        typee=input("Enter your type of book (Story/Novel/Educational): ")
        self.typee=typee
        print("You have choosen ",self.typee)
        subtypee=input("Enter your subtype(Story-(Kids/Adults),Novel-(Crime/Drama),Educational-(GK/Vocabulory): )")
        self.subtypee=subtypee
        print("You have choosen ",self.subtypee)
class Typee(Books):
    def Story(self):
        if self.typee=="Story" and self.subtypee=="Kids":
            kb=input("Enter the name of the book: ")
            self.kb=kb
            kbc="1111"
            kbc1=""
            self.kbc=kbc
            self.kbc1=kbc1
            while kbc1!=kbc:
                kbc1=input("Enter the code of the book: ")
            print("The book ",self.kb,"with the code ",self.kbc,"is available")
        elif self.typee=="Story" and self.subtypee=="Adults":
            ab=input("Enter the name of the book: ")
            self.ab=ab
            abc="2222"
            abc1=""
            self.abc=abc
            self.abc1=abc1
            while abc1!=abc:
                abc1=input("Enter the code of the book: ")
            print("The book ",self.ab,"with the code ",self.abc,"is available")
    def Novel(self):
        if self.typee=="Novel" and self.subtypee=="Crime":
            cb=input("Enter the name of the book: ")
            self.cb=cb
            cbc="3333"
            cbc1=""
            self.cbc=cbc
            self.cbc1=cbc1
            while cbc1!=cbc:
                cbc1=input("Enter the code of the book: ")
            print("The book ",self.cb,"with the code ",self.cbc,"is available")
        elif self.typee=="Novel" and self.subtypee=="Drama":
            db=input("Enter the name of the book: ")
            self.db=db
            dbc="4444"
            dbc1=""
            self.dbc=dbc
            self.dbc1=dbc1
            while dbc1!=dbc:
                dbc1=input("Enter the code of the book: ")
            print("The book ",self.db,"with the code ",self.dbc,"is available")
    def Educational(self):
        if self.typee=="Educational" and self.subtypee=="GK":
            gb=input("Enter the name of the book: ")
            self.gb=gb
            gbc="5555"
            gbc1=""
            self.gbc=gbc
            self.gbc1=gbc1
            while gbc1!=gbc:
                gbc1=input("Enter the code of the book: ")
            print("The book ",self.gb,"with the code ",self.gbc,"is available")
        elif self.typee=="Educational" and self.subtypee=="Vocabulory":
            vb=input("Enter the name of the book: ")
            self.vb=vb
            vbc="2222"
            vbc1=""
            self.vbc=vbc
            self.vbc1=vbc1
            while vbc1!=vbc:
                vbc1=input("Enter the code of the book: ")
            print("The book ",self.vb,"with the code ",self.vbc,"is available")
T=Typee()
T.preference()
T.Story()
T.Novel()
T.Educational()

 
#tuple

customers=("Dhanya","Nitin","Aadya")
c=input("Have you already been here? ")
if c=="Yes":
    print(customers)
    c1=input("Is your name here? ")
    if c1=="Yes":
        print("Thank you for your answer!")
    else:
        n=input("Enter your name again: ")
        customer=list(customers)
        customer.append(n)
        customers=tuple(customer)
        print("New list of custoners")
        print(customer)
else:
    n=input("Enter your name: ")
    customer=list(customers)
    customer.append(n)
    customers=tuple(customer)
    print("New list of custoners")
    print(customer)
dob=int(input("Enter your Birth Year: "))
s=200
if dob>2005:
    print("Usual monthly library subscription of our library is: ",s )
    print("Since you're age is less than 21, your have a discount of 30/- in your subscription")
    ss=s-30
    print("Your monthly library subscription is ",ss)
else:
    print("Your monthly library subscription is: ",s)
    
    
#overriding

class Lan:
    def new(self,c):
        self.c=c
        print("'''''''''''''''''''''''''''''''''''''''''''")
        print("Launching Soon....")
        print("New launch in Stories - ",c)
class Nov(Lan):
    def new(self,c):
        self.c=c
        print("New lanuch in Novels - ",c)
class Eduu(Lan):
    def new(self,c):
        self.c=c
        print("New launch in Educational - ",c)
        print("'''''''''''''''''''''''''''''''''''''''''''")
l=Lan()
l.new("Classics")
n=Nov()
n.new("Horror")
e=Eduu()
e.new("Skills")


#abstration

from abc import ABC
class fair(ABC):
    def lib(self):
        print("Advertisement:")
        print("-------------------------------------------------------------------------------------------")
        print("City Central Library presents,'The Readers Fete', a fun book fair for people of all ages!")
class time(fair):
    def lib(self):
        print("Timings 9:00 am to 5:00 pm ,Date:20/06/2026")
class entry(fair):
    def lib(self):
        print("Free Entry for all !!")
        print("-------------------------------------------------------------------------------------------")
        print("Thank You for Visiting Our Library!!")
        print("Visit Again!!")
f=fair()
f.lib()
t=time()  
t.lib()
e=entry()
e.lib()

