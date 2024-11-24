#zad1
from modules import geometria
from modules import temperatura

promien = 16

obwod = geometria.obwod_kola(promien)
pole = geometria.pole_kola(promien)

print(f"obwod_kola = {obwod}")
print(f"pole_kola = {pole}")


#zad 2
#----------------------------------------------------------------
print(temperatura.c_to_f(21))
print(temperatura.f_to_c(89))
print(temperatura.c_to_k(35))

#zad 3
#----------------------------------------------------------------
# zad 3 w cwiczenia.py


#zad 4
#----------------------------------------------------------------
import random
Szcesliwa_liczba = random.randint(1, 100)
print(Szcesliwa_liczba)
Rocznik = [2000, 2001, 2002, 2003]
Rocznik_lucky = random.choice(Rocznik)
print(Rocznik_lucky)


#zad 5
#----------------------------------------------------------------
import random
kule = list(range(1, 50))
print("Lista kul", kule)
print("Wylosowane kule", sorted(random.sample(kule, 6)))


#zad 6
#----------------------------------------------------------------
import time
czas = int(input("Podaj czas w sc:"))
for secund in range(czas, 0, -1):
    print(f"Pozostalo {secund} secund")
    time.sleep(1)
print("Koniec obliczenia")


#zad 7
#----------------------------------------------------------------
from datetime import datetime

last_lab_date = datetime(2024, 11, 19)
exam_date = datetime(2024, 12, 17)

current_date = datetime.now()
days_since_last_lab = (current_date - last_lab_date).days
days_until_exam = (exam_date - current_date).days

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

print(f"Days since the last laboratory: {days_since_last_lab} days")
print(f"Days until the exam: {days_until_exam} days ({month_names[exam_date.month]})")


#zad 8
#----------------------------------------------------------------
import keyword

lista = ["for", "print", "break", "done", "bad"]
for slowo in lista:
    if keyword.iskeyword(slowo):
        print(slowo, "jest slowem kluczowym")
    else:
        print(slowo, "nie jest slowem kluczowym")

#zad 9
#----------------------------------------------------------------
import math
import keyword

math_functions = dir(math)
keyword_functions = dir(keyword)
print("math module function:")
print(math_functions)
print("keyword module function:")
print(keyword_functions)

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
