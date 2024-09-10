class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

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

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError(f'Expected type {type(self).__name__}, got {type(other).__name__} instead')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            raise TypeError(f'Expected type int, got {type(value).__name__} instead')

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
            return self
        else:
            raise TypeError(f'Expected type int, got {type(value).__name__} instead')

    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors /= value
            return self
        else:
            raise TypeError(f'Expected type int, got {type(value).__name__} instead')

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            raise TypeError(f'Expected type int, got {type(value).__name__} instead')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)