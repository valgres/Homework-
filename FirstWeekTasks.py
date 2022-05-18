# Task1

a = int(input())
b = int(input())
c = int(input())
p = float(a + b + c)/2 # полупериметр треугольника
print((p * (p-a) * (p-b) * (p-c)) ** 0.5)


# Task2

a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
    print(True)
else:
    print(False)

# Task3

a = float(input())
b = float(input())
c = input()
if (c == "/" or c == "mod" or c == "div") and b == 0:
    print('Деление на 0!')
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/" and b != 0:
    print(a / b)
elif c == "mod" and b != 0:
    print(a % b)
elif c == "pow":
    print(a ** b)
elif c == "div" and b != 0:
    print(a // b)

# Task4

figure = str(input())
if figure == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = float(a + b + c) / 2  # полупериметр треугольника
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
if figure == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a * b)
if figure == 'круг':
    r = int(input())
    print(3.14 * r * r)

# Task5

a, b, c = int(input()), int(input()), int(input())

mx = max(a, b, c)
mn = min(a, b, c)
last = (a + b + c) - mx - mn

print(mx, mn, last, sep='\n')

# Task6

amountOfEngineers = int(input())
p = amountOfEngineers % 10
if p in (0, 5, 6, 7, 8, 9) or ((amountOfEngineers % 100) // 10) == 1:
    print(amountOfEngineers, 'программистов')
elif amountOfEngineers % 10 == 1:
    print(amountOfEngineers, 'программист')
else:
    print(amountOfEngineers, 'программиста')

# Task7

ticketNumber = int(input())
firstHalf = ((ticketNumber % 10) + ((ticketNumber % 100) // 10) + ((ticketNumber % 1000) // 100))
secondHalf = (((ticketNumber // 1000) % 10) + ((ticketNumber // 10000) % 10) + ((ticketNumber // 100000) % 10))
if firstHalf == secondHalf:
    print('Счастливый')
else:
    print('Обычный')
