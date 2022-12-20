# Реализовать программу работы с органическими клетками, состоящими из ячеек.
#
# Необходимо создать класс Клетка (Cell).
#
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
#
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).
#
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Произошло объединение. Итог: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Результат при вычитании: {sub} ' if sub > 0 else 'Получено отрицательное значение'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity




cell = Cell(35)
cell_two = Cell(10)
print(cell + cell_two)
print(cell - cell_two)
print(cell * cell_two)
print(cell / cell_two)
