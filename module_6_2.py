class Vehicle:
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ['Красный', 'Белый', 'Чёрный', 'Синий', 'Зеленый','black']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return ( f"Модель: {self.__model}")

    def get_horsepower(self):
        return ( f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return (f"Цвет: {self.__color}")

    def print_info(self):
        print(f"\n{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}")

    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                print( self.__color)
                break

        print( f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
