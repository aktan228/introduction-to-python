# 1 int() -> 1, 4, 6 (целые числа)
# 2 str() -> "text" (текс)
# 3 float() -> 1.23, 12.4357, 3.14 (не целые числа)
# 4 bool() -> true/false
#
# num1 = float(input('insert 1 num:'))
# num2 = float(input('insert 2 num:'))
#
# summa = (num1 + num2)
# minus = (num1 - num2)
#
# print(num1, "+", num2, "=>", summa, '=', int(summa))
# print("minus: ", minus)

# a = 5.12 #float
# print(a)
#
# b = int(a) #int
# print(b)
#
# print(f"a = {a}, b = {b}, the sum = {a+b}")

# name = input('insert name: ')
# age = input('How old are u?: ')
# film = input('Which your favorite film?: ')
# book = input('which your favorite book?: ')
#
# print(f"Your name is {name}, u {age} y.o, your favorite film is {film} and your favorite book is {book}")

apple = 60
sugar = 80
pineapple = 400
banana = 240
orange = 250

budget = float(input("Say your budget"))
applePrice = float(input("How many kg apple you take: "))
sugarPrice = float(input("How many kg sugar you take: "))
pineapplePrice = float(input("How many kg pineapple you take: "))
bananaPrice = float(input("How many kg banana you take: "))
orangePrice = float(input("How many kg orange you take: "))

appleConc = apple * applePrice
sugarConc = sugar * sugarPrice
pineappleConc = pineapple * pineapplePrice
orangeConc = banana * bananaPrice
bananaConc = orange * orangePrice
allConc = appleConc + sugarConc + pineappleConc + orangeConc + bananaConc
print(f"You take "
      f"{applePrice}kg of apple - {appleConc}, \n"
      f"{sugarPrice}kg of sugar - {sugarConc}, \n"
      f"{pineapplePrice}kg of pineapple - {pineappleConc}, \n"
      f"{bananaPrice}kg of banana - {orangeConc}, \n"
      f"{orangePrice}kg of orange - {bananaConc}. \n"
      f"You have to pay {allConc}.\n"
      f"{budget - allConc} your change")