# height = float(input('Введите ваш рост'))
# print(height)
#
# print(type(height))

# name = 'Tom'
# isStudent = True
# isMarried = False
# height = int(input('insert ypur height'))
# print(height)
# print(type(isStudent))

"""
HomeWork
"""

# print("hello please answer for the question?")
# humanIsAlive = True
# data = input("which day today")
# president = input("Name of our president")
# calc = int(input('If u sum 17 and 25 which result u get?'))
#

# weight = float(input("Введите ваш вес (кг): "))
# bench = float(input("Сколько вы жмёте лёжа (кг): "))
# squat = float(input("Сколько вы приседаете (кг): "))
# deadlift = float(input("Сколько вы тянете (кг): "))
#
# sumAll = int(bench + squat + deadlift)
# avgWeight = int(sumAll / 3)
# print("\nВаши результаты:")
# print(f"Вес тела: {weight} кг")
# print(f"Жим лёжа: {bench} кг")
# print(f"Присед: {squat} кг")
# print(f"Становая тяга: {deadlift} кг")
# print(f"Суммарный подъём: {sumAll} кг")
# print(f"Средний подъём: {deadlift:.2f} кг")
#

distance = int(input("Введите расстояние (км): "))
time = float(input("Введите время в пути (ч): "))
speed = distance / time
print(f"Средняя скорость автомобиля: {speed} км/ч")

message = ["Скорость не превышена.", "Скорость превышена!"][speed > 60]
print(message)
