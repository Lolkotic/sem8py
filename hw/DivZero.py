# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


from sys import exit
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        # exit(1)


inp_data = input("150//your number" + "\n" + "Write your number here, please: ")

try:
    inp_data = int(inp_data)
    res = 150 // inp_data
except ZeroDivisionError:
    print("You can't divide by zero. Try again, please")
else:
    print(f"Everything is  ok. The result is - {res}")
finally:
    print("Thank you! The end of the programme")

