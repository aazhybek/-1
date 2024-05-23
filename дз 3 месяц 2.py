class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и сеттеры
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # Метод для вычислений
    def make_computations(self):
        return self.__cpu * self.__memory

    # Переопределение __str__
    def __str__(self):
        return f"Компьютер: CPU = {self.__cpu}, Память = {self.__memory}"

    # Переопределение магических методов сравнения
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттеры и сеттеры
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    # Метод для симуляции звонка
    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты")

    # Переопределение __str__
    def __str__(self):
        return f"Телефон с SIM-картами: {', '.join(self.__sim_cards_list)}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод для симуляции использования GPS
    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    # Переопределение __str__
    def __str__(self):
        return f"Смартфон: CPU = {self.cpu}, Память = {self.memory}, SIM-карты: {', '.join(self.sim_cards_list)}"

# Создание объектов
computer = Computer(3.5, 16)
phone = Phone(["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(2.8, 8, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(3.2, 12, ["O!", "Beeline"])

# Печать информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестирование методов каждого объекта
print("\n--- Вычисления на компьютере ---")
print(computer.make_computations())

print("\n--- Звонок с телефона ---")
phone.call(1, "+996 777 99 88 11")

print("\n--- Методы смартфона ---")
smartphone1.use_gps("Ош")
smartphone1.call(2, "+996 555 55 55 55")
print(smartphone1.make_computations())

print("\n--- Магические методы ---")
print(computer == smartphone1)
print(computer != smartphone1)
print(computer < smartphone2)
print(computer <= smartphone2)
print(computer > smartphone1)
print(computer >= smartphone1)
