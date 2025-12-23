class Car:
    def __init__(self,color : str,type : str,mileage : float,seat_capacity:int) -> None:
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"Seat_capacity = {self.seat_capacity}")


# c1 = Car("Black","Petrol",22.5,4)  
# c1.base_info()

class Audi(Car):
    def __init__(self) -> None:
        print("Audi INIT")

c1 = Audi()
c1.color = "Black"
c1.type = "Petrol"
c1.mileage = 22.5
c1.seat_capacity = 4
c1.base_info()