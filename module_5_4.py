# Различие атрибутов класса и экземпляра
# Задача  "История строительства"

class House:
    houses_history = []  # общий список зданий

    def __new__(cls, *args, **kwargs):
        # добавление нового здания в общий список
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):  # удаление объекта
        print(self.name, ' снесён, но он останется в истории')


House_1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

House_2 = House('ЖК Лесное', 20)
print(House.houses_history)

House_3 = House('ЖК Луговое', 15)
print(House.houses_history)

del House_2
del House_3
print(House.houses_history)
