#zad 10
#----------------------------------------------------------------
import random

start = int(input("Enter the start of range"))
end = int(input("Enter the end of range:"))

temp_list = []
for i in range(10):
    temp_list.append(random.randint(start, end))

numbers = tuple(temp_list)
print("Generated tuple:", numbers)

product = 1
for num in numbers:
    product *= num

geometric_mean = product ** (1 / len(numbers))
print("geometric_mean:", geometric_mean)
