from sample import Car
class Dealership:
    def __init__(self, inventory=[], capacity=10 ):
        self.inventory = inventory
        self.capacity = capacity
        
    def getInventory(self):
        for car in self.inventory:
            print(car.getCar())
            
if __name__ == '__main__':
    car1 = Car('Honda', 'Civic')
    car2 = Car('toyota', 'corolla')
    cars = []
    cars.append(car1)
    cars.append(car2)
    
    dealership = Dealership(cars, 5)
    
    print('bro here')
    dealership.getInventory()