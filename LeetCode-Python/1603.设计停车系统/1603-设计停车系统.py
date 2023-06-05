class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b, self.m, self.s = big, medium, small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.b:
                self.b -= 1
                return True
            return False
        elif carType == 2:
            if self.m:
                self.m -= 1
                return True
            return False
        elif carType == 3:
            if self.s:
                self.s -= 1
                return True
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)