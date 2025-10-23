numbers = {1, 2, 3, 3, 2}
print(numbers)  


numbers.add(4)
numbers.discard(2)
print(numbers)


a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  
print(a & b)  
print(a - b)  


print(True)
print(False)
print(None)

text = "Python"
print("Довжина :", len(text))

numbers = [3, 7, 1, 9, 5]
print("Макс:", max(numbers))
print("Мін:", min(numbers))

numbers = [10, 20, 30]
print("Сума чисел:", sum(numbers))



idk = ["предмет", "людина", "сила"]

for idk in idk:
    print("Типу це", idk)

count = 1

while count <= 5:
    print("Номер", count)
    count += 1


for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")



age = 18

if age >= 18:
    print("Повноліття")
else:
    print("Неповноліття")


temperature = 10

if temperature > 25:
    print("Сьогодні спекотно ")
elif temperature > 15:
    print("Сьогодні тепло ")
elif temperature > 5:
    print("Прохолодно ")
else:
    print("Холодно ")


x = 5

if x > 0:
    if x % 2 == 0:
        print("Додатне парне число")
    else:
        print("Додатне непарне число")
else:
    print("Число не є додатним")



try:
    x = 10
    y = 0
    result = x / y
    print("Результат:", result)
except ZeroDivisionError:
    print("Ділення на нуль неможливе")
finally:
    print("у будь-якому випадку.")


try:
    number = int("Python")  
    print("Число:", number)
except ValueError:
    print("Неможливо перетворити рядок у число.")
finally:
    print("Обробка завершена.")




with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("Hell yeah")


print("Ready")


with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Inside: ")
    print(content)


sum_lambda = lambda a, b: a + b
print(sum_lambda(3, 7))

square_lambda = lambda x: x ** 2
print(square_lambda(5))


name = "Олена"      # рядок (str)
age = 25            # ціле число (int)
height = 1.68       # число з плаваючою комою (float)
is_student = True   # логічне значення (bool)

print(name, age, height, is_student)

score = 85

if score >= 90:
    print("Відмінно!")
elif score >= 70:
    print("Добре!")
else:
    print("Потрібно підтягнути знання.")

# цикл for
for i in range(5):
    print("Крок", i)

# цикл while
count = 0
while count < 3:
    print("Рахунок:", count)
    count += 1

fruits = ["яблуко", "банан", "вишня"]
fruits.append("ківі")
fruits.remove("банан")
print("Мої фрукти:", fruits)
