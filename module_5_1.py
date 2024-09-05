
class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        for floor in range(1, new_floor + 1):
            if new_floor < 1 or new_floor > self.number_of_floors:
                print(f'{new_floor}-го этажа не существует')
                break
            if floor == new_floor:
                print(f'Приехали. {new_floor}-ый этаж')
                break
            print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(20)

