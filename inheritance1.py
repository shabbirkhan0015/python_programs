class vehicle:
       distance=50
       def __init__(self,model,r_number,speed,fuel,fuel_cons):
           self.model=model
           self.r_number=r_number
           self.speed=speed
           self.fuel=fuel
           self.fuel_cons=fuel_cons
       def fuelneeded(self,distance):
           f=0
           f=self.distance/self.fuel_cons
           print('FUEL NEEDED:',f)
       def distanceCovered(self,time):
           d=0
           d=self.speed*self.time
           print(d)
       def display(self):
           print('model:',self.model)
           print('registration number:',self.r_number)
           print('Speed:',self.speed)
           print('fuel capacity:',self.fuel)
           print('fuel consumption:',self.fuel_cons)
class bus(vehicle):
    no_passenger=200
    def __init__(self,model,r_number,speed,fuel,fuel_cons,no_passenger):
           self.no_passenger=no_passenger
           vehicle.__init__(self,model,r_number,speed,fuel,fuel_cons) 
    def display(self):
           print('model:',self.model)
           print('registration number:',self.r_number)
           print('Speed:',self.speed)
           print('fuel capacity:',self.fuel)
           print('fuel consumption:',self.fuel_cons)
           print('passenger:',self.no_passenger)
           
class truck(vehicle):
    
    def __init__(self,model,r_number,speed,fuel,fuel_cons,caroWeight):
           self.cargoWeight=caroWeight           
           vehicle.__init__(self,model,r_number,speed,fuel,fuel_cons)
    def display(self):
           print('model:',self.model)
           print('registration number:',self.r_number)
           print('Speed:',self.speed)
           print('fuel capacity:',self.fuel)
           print('fuel consumption:',self.fuel_cons)
           print('caroweight limit:',self.cargoWeight)
class transport:
    print("-----------FOR TRUCK------------------------")
    t1=truck(111,345,40,50,25,100)
    t1.display()
    print("----------------FOR BUS--------------------")
    t2=bus(111,345,40,50,25,100)
    t2.display()
    v=vehicle(111,345,50,40,25)
    v.fuelneeded(50  )
    
t=transport()
    