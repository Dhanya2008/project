print("Trinay Hospital......","\nYour Health is Our Priority","\n....................")

#constructor
#error handling
#create
class New:
    def __init__(self):
        patient_name=input("Enter the name of the patient: ")
        try:
            patient_age=int(input("Enter the age of the patient: "))
        except ValueError:
            print("Invalid input. Please enter a valid age.")
            patient_age=int(input("Enter the age of the patient: "))
        date_admitted=input("Enter the date of admission (DD/MM/YYYY): ")
        patient_phone=input("Enter the phone number of the patient: ")
        self.patient_name=patient_name
        self.patient_age=patient_age
        self.date_admitted=date_admitted
        self.patient_phone=patient_phone
    def display(self):
                print("Patient Details:")
                print("Patient Name:",self.patient_name)
                print("Patient Age:",self.patient_age)
n1=New()
n1.display()  
 
 # Treatment of the patient
 #Hirerarchical inheritance
 # polymorphism-overriding
class Patient:
    def condition(self):
        print("Treatment for the patient")
    def consult(self):
        specialist=input("Do you want to consult with a specialist for your treatment ? ")
        self.specialist=specialist
        if self.specialist=="Yes":
            print("You will be connected to a specialist for your treatment.")
            print(" Consulting with the specialist..............................")
            print("As your consultation is over, you can proceed with your treatment..")
        else:
            print("Since you have chosen not to consult with a specialist, you can proceed with your treatment..")
        cause_of_admission=input("Enter the cause of admission of the patient: ")
        self.cause_of_admission=cause_of_admission
        patient_condition=input("Enter the condition of the patient again: ")
        self.patient_condition=patient_condition
class Treatment1(Patient):
    def condition(self):
        if self.patient_condition=="Stable":
            print("As you are stable there is no need to get admitted, You can wait for your turn and meet the doctor..","\nObservation of patient...")
            if self.cause_of_admission=="Fever" or self.cause_of_admission=="Cold" or self.cause_of_admission=="Cough":
            #meeting the doctor
                print("You are affected by the usual flu symptoms..","\n You can buy the prescibed medicine in the pharmacy","\n Take the medicines on time and rest well.. You will be alright..")
            elif self.cause_of_admission=="Injury":
                injury=input("Mention the place where your injured: ")
                self.injury=injury
                if self.injury=="Head":
                    print("You have a head injury.. As you are stable,lets examine your wound.......","\n You have a minor injury.","\n Do not remove your bandage to prevent infection..","\n Take the prescribed medicines on time and rest well.. You will be alright..")
                elif self.injury=="Leg":
                    print("You have a leg injury.. As you are stable,lets examine your wound.......","\n You have a minor injury.","\n Do not remove your bandage to prevent infection..","\n Take the prescribed medicines on time and rest well.. You will be alright..")
                elif self.injury=="Hand":
                    print("You have a hand injury.. As you are stable,lets examine your wound.......","\n You have a minor injury.","\n Do not remove your bandage to prevent infection..","\n Take the prescribed medicines on time and rest well.. You will be alright..")  
                else:
                    print("You have a minor injury.. As you are stable,lets examine your wound.......","\n Not a serious injury.","\n Do not remove your bandage to prevent infection..","\n Take the prescribed medicines on time and rest well.. You will be alright..")   
            else:
                print("Just a normal illness.. You can buy the prescibed medicine in the pharmacy","\n Take the medicines on time and rest well.. You will be alright..")
class Treatment2(Patient):
    def condition(self):
        if self.patient_condition=="Moderate":
            print("As you are in moderate condition, you will be admitted for further observation and treatment..")
            if self.cause_of_admission=="Fever" or self.cause_of_admission=="Cold" or self.cause_of_admission=="Cough" or self.cause_of_admission=="Body pain":
               print("You are affected with viral fever..You will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 2-3 days and take the prescribed medicines on time..","\n You will be alright soon..") 
            elif self.cause_of_admission=="Injury":
                injury=input("Mention the place where your injured: ")
                self.injury=injury
                if self.injury=="Head":
                    print("You have a head injury.. As you are in moderate condition, you will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for a week and take the prescribed medicines on time..","\n You will be alright soon..")
                elif self.injury=="Leg":
                    print("You have a leg injury.. As you are in moderate condition, you will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 2-3 days and take the prescribed medicines on time..","\n You will be alright soon..")
                elif self.injury=="Hand":
                    print("You have a hand injury.. As you are in moderate condition, you will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 2-3 days and take the prescribed medicines on time..","\n You will be alright soon..")  
                else:
                    print("You have a minor injury.. As you are in moderate condition, you will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 2-3 days and take the prescribed medicines on time..","\n You will be alright soon..")  
            else:
                print("Just a normal illness.. You will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 2-3 days and take the prescribed medicines on time..","\n You will be alright soon..")    
class Treatment3(Patient):
    def condition(self):
        if self.patient_condition=="Critical":
            print("As you are in critical condition, you will be admitted in the emergency ward for further observation and treatment..")
            if self.cause_of_admission=="Fever" or self.cause_of_admission=="Cold" or self.cause_of_admission=="Cough" or self.cause_of_admission=="Body pain":
               print("You are affected with severe flu..","\nObservation of patient......","\n You are in stable condition now...","But you are advised to stay in the hospital for a week for further treatment.","\n Once you are alright, you will be discharged from the hospital..")
            elif self.cause_of_admission=="Injury":
                injury=input("Mention the place where your injured: ")
                self.injury=injury
                if self.injury=="Head":
                    print("You have a severe head injury..","\nObservation of patient......","\n You are in stable condition now...","But you are advised to stay in the hospital for 2 weeks for further treatment.","\n Once you are alright, you will be discharged from the hospital..")
                elif self.injury=="Leg":
                    print("You have a severe leg injury..","\nObservation of patient......","\n You are in stable condition now...","But you are advised to stay in the hospital for 1 week for further treatment.","\n Once you are alright, you will be discharged from the hospital..")
                elif self.injury=="Hand":
                    print("You have a severe hand injury..","\nObservation of patient......","\n You are in stable condition now...","But you are advised to stay in the hospital for 1 week for further treatment.","\n Once you are alright, you will be discharged from the hospital..")
                else:
                    print("You have a severe injury..","\nObservation of patient......","\n You are advised to stay in the hospital for 1 week and take the prescribed medicines on time..","\n You will be alright soon..")  
            else:
                print("A severe  illness.. You will be admitted for further observation and treatment..","\nObservation of patient....","\n You are advised to stay in the hospital for 1 week and take the prescribed medicines on time..")
#read
condition = input("Enter the condition of the patient: ")
if condition == "Stable":
    patient = Treatment1()
elif condition == "Moderate":
    patient = Treatment2()
else:
    patient = Treatment3()

patient.consult()
patient.condition()

#Giving special pass to the patients
#list
#update
#delete
hos=input("Do you want patient's special pass ? ")
if hos=="Yes":
    special_pass=["Food","Medicine","Room"]
    items=3
    print("The things included in the special pass")
    for i in special_pass:
        print(i)
    print("Total number of items in the special pass: ",items)
    s_pass=input("Do you want to add or remove any things from the pass? ")
    if s_pass=="Add":
        n=input("Enter the item you want to add in the pass: ")
        special_pass.append(n)
        items+=1
        print("New list of special passes")
        print(special_pass)
        print("Total number of items in the special pass: ",items)
    elif s_pass=="Remove":
        n=input("Enter the item you want to remove from the pass: ")
        special_pass.remove(n)
        items-=1
        print("A new list of special passes")
        print(special_pass)
        print("Total number of items in the special pass: ",items)
    else:
        print("No changes made to the special pass.")
        print("List of things included in the special pass")
        print(special_pass)
        print("Thank You")
else:
    print("No special pass is provided for the patient.")
    print("Thank You")
    
#Adding patients to the ward    
#abstraction
from abc import ABC
class Hospital(ABC):
    def patients(self):
        total_patients=0
        print("----------------------------------------------------")
        print("Adding patients to the ward by the hospital staff...")
        self.total_patients=total_patients
        while self.total_patients<=4:
            patient_id=input("Enter the patient ID: ")
            self.patient_id=patient_id
            self.total_patients+=1
            print(f"Patient added: {self.patient_id}")
            print(f"Total patients allowed in the ward: {self.total_patients}")
class Ward(Hospital):
    def patients(self):
        super().patients()
        print("All patients have been added to the ward.")
h=Ward()
h.patients()
           
#total patient record for the day            
#polymorphism-overloading
print("-----------------------------------------------------")
print("Total patient record for the day...")
class entire:
    def pat(self,today):
        self.today=today
        print("No.of patients visited the hospital today: ",self.today)
    def pat(self,today,discharged):
        self.today=today
        self.discharged=discharged
        print("No.of patients visited the hospital today: ",self.today)
        print("No.of patients discharged from the hospital today: ",self.discharged)
    def pat(self,today,discharged,totall):
        self.today=today
        self.discharged=discharged
        self.totall=totall
        print("No.of patients visited the hospital today: ",self.today)
        print("No.of patients discharged from the hospital today: ",self.discharged)
        print("Total no.of patients in the hospital today: ",self.totall)
e=entire()
e.pat(80,30,50)

#Advertisement for the newly opening hospital
#multilevel inheritance
#
class Advertisement:
    def ad1(self):
        print("**************************************************************************")
        print("We are proud and happy to announce the opening of our new hospital...")
        print("Trinay Children's Multispeciality Hospital...","\n Our hospital is opening soon to serve the community with the best healthcare services for children.")
class Services(Advertisement):
    def ad2(self):
        print("Our hospital will provide a wide range of sevices like:")
        services={"Pediatrics","Pediatric Surgery","Pediatric Cardiology","Pediatric Neurology"} 
        self.services=services
        for i in self.services:
            print(i)
class Facilities(Services):
    def ad3(self):
        print("Our hospital will also provide the following facilities:")
        facilities={"24/7 Emergency Services","Advanced Diagnostic Facilities","Child-Friendly Environment","Experienced Pediatric Specialists"}
        self.facilities=facilities
        for i in self.facilities:
            print(i)     
        print("We are committed to providing the best healthcare services for children and ensuring their well-being...","\n Launching Soon...")
        print("**************************************************************************")
f=Facilities()
f.ad1()
f.ad2()
f.ad3()       

#create file

new_hospital=open("./Child_hospital.txt","w")
print("File is created",new_hospital.name)
new_hospital.write(" Our new - Trinay Children's Multispeciality Hospital launching soon....")
new_hospital.close()