class House:
    def __init__(self,name,num):
        self.name = name
        self.number_of_floors = num
    def go_to (self,new_floor):
        self.new_floor = new_floor
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for floor in range(1,new_floor +1):
                print(floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)