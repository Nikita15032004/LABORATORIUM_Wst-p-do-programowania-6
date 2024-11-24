#zad 6
#----------------------------------------------------------------
import time
czas = int(input("Podaj czas w sc:"))
for secund in range(czas, 0, -1):
    print(f"Pozostalo {secund} secund")
    time.sleep(1)
print("Koniec obliczenia")
