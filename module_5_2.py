#Задача "Магические здания":
#Для решения этой задачи будем пользоваться решением к предыдущей задаче.
#Необходимо дополнить класс House следующими специальными методами:
#__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#Пример выполняемого кода:
#h1 = House('ЖК Эльбрус', 10)
#h2 = House('ЖК Акация', 20)
# __str__
#print(h1)
#print(h2)
# __len__
#print(len(h1))
#print(len(h2))
# Решение:

class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        if 1 > new_floor or self.number_of_floors < new_floor:
            print("Такого этажа не существует")
            return
        else:
            for i in range(1, new_floor +1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))