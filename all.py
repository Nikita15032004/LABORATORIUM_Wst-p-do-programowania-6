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



