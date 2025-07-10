class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model
    
    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.model = model
        
    def getCar(self):
        return [self.make, self.model]
    
if __name__ == '__main__':
    car1 = Car('Honda', 'Civic')
    car2 = Car('toyota', 'corolla')
    
    cars = []
    cars.append(car1)
    cars.append(car2)
    
    print('Cars:')
    for car in cars:
        print(car.getCar())
        
    car1.setMake('Changed here')
    
     
    print('new try Cars:')
    for car in cars:
        print(car.getCar())
