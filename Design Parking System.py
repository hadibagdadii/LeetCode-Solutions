class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_spots = big
        self.medium_spots = medium
        self.small_spots = small 

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_spots > 0:
            self.big_spots -= 1
            return True
        elif carType == 2 and self.medium_spots > 0:
            self.medium_spots -= 1
            return True
        elif carType == 3 and self.small_spots > 0:
            self.small_spots -= 1
            return True
        return False
