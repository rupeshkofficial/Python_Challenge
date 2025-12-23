class Car:
    def set_info(self,color : str,type : str,mileage : float,seat_capacity:int) -> None:
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"Seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def set_audi_info(self,electric:bool,city: str) -> None:
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")
        print("Audi INIT")

c1 = Audi()
c1.set_info("Black","Petrol",12.2,4)
c1.set_audi_info(True,"Mumbai")
c1.audi_info()
c1.audi_info()