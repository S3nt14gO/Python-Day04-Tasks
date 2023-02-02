import re
class person:
    healthRate = 100

    moods = ('Happy','Tired','Lazy')

    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.__money = money
        self.__mood = mood
        self.__healthRate = healthRate
    @classmethod

    def sleepTime(self,sleep):
        if (sleep > 7):
            self.__mood = person.moods[0]
        elif (sleep < 7):
            self.__mood = person.moods[1]
        else:
            self.__mood = person.moods[2]
    def eatTime(self, eat):
        if eat > 3:
            print("Enough meals !!!")
        elif (eat == 3):
            self.__healthRate = 100
        elif (eat == 2):
            self.__healthRate = 75
        elif (eat == 1):
            self.__healthRate = 50
        else:
            print("so Hungry :( ")

    def buyItems(self,buy):
        self.__money= self.__money-(buy*10)

class Employee(person):
    def __init__(self, Empid, car, email, salary, distanceToWork ):
        self.Empid = Empid
        self.car = car
        self.__email = email
        self.__salary=salary
        self.__distanceToWork = distanceToWork
    @property
    def Salary(self):
        return self.__salary

    @Salary.setter
    def Salary(self, newSalary):
        if (newSalary >= 1000):
            self.__salary = newSalary
        else:
            print ("Modern Slave with a suit !!")

    @classmethod
    def workTime(self,work):
        if (work > 8):
            self.mood = person.moods[0]
        elif (work < 8):
            self.mood = person.moods[1]
        else:
            self.mood = person.moods[2]

    def sendEmail(self):
        Pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if(re.match(Pattern, self.__email)==1):
            print("Email Checked")

    def Drive(self, distance,time):
        runCar= Car(velocity=distance/time)
        print ("Drive to work with verlocity = ",runCar," and distance ",distance,"K.m per ",time)

    def GasTank(self):
        self.__fuelRate = Car.gasAmount


class Office(Employee):
    allEmployees = {}
    noOfEmployees = 0
    reward =0
    def __init__(self ,OrgName , employees ):
        self.OrgName = OrgName
        self.employees = employees
        Office.noOfEmployees += 1

    @classmethod

    def hire(self,name ,employees):
        self.OrgName = name
        self.employees = employees

    def fire(self,name):
        del Office.allEmployees[id]

    def CheckLateness(self,empid , moveHours):
        if (moveHours > 9):
            for emp in self.Empid:
                if emp == empid:
                    self.reward -= 10

        elif (moveHours < 9):
            for emp in self.Empid:
                if emp == empid:
                    self.reward += 10
        else:
            print("Just on time")
    def CalculateLateness (self, move, distance, velocity):
        hours = distance/velocity
        moveHours = move + hours
        print("will arrive at ",moveHours," O,clock")

    def rewardEmp(self,empid,reward):
        for emp in self.Empid:
            if emp == empid:
                self.__salary += reward


    def deductEmp(self,empid,deduct):
        for emp in self.Empid:
            if emp == empid:
                self.__salary -= deduct


    def get_all_Employees(self):
        Office.allEmployees[self.OrgName]=[]
        Office.allEmployees[self.OrgName].append(self.employees)
        print(Office.allEmployees)
        print("The number of Employees : ",Office.noOfEmployees)

    def get_All_Employee_ID(self):
        print(Office.allEmployees[self.OrgName])


class Car(Employee):

    def __init__(self, CarName,fuelRate, velocity):
        self.CarName = CarName
        self.__fuelRate = fuelRate
        self.__velocity = velocity


    @classmethod
    def Run(self, distance):
        self.__fuelRate= self.__fuelRate - distance
        if self.__fuelRate == 0:
             self.__velocity = 0
             print("Out of Fuel !")

    def stop(self):
        self.__velocity = 0






