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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))