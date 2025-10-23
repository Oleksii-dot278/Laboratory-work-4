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
