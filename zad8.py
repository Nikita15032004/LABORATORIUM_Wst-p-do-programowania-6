#zad 8
#----------------------------------------------------------------
import keyword

lista = ["for", "print", "break", "done", "bad"]
for slowo in lista:
    if keyword.iskeyword(slowo):
        print(slowo, "jest slowem kluczowym")
    else:
        print(slowo, "nie jest slowem kluczowym")
