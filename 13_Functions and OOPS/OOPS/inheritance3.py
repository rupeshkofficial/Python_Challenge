class Car:
    def set_info(self):
        self.color = input("Enetr car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"Seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def set_audi_info(self):
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

c1 = Audi()
c1.set_info()
c1.set_audi_info()
c1.base_info()
c1.audi_info()
