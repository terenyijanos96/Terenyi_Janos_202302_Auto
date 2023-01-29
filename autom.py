from Auto import *


def beolvas_eltarol():
    f = open("auto.txt", "r", encoding="utf-8")
    fejlec, tartalom = f.readline(), f.readlines()
    f.close()

    auto_lista = []
    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("$")
        auto_lista.append(Auto(sor))
        i += 1

    return auto_lista


def flotta(auto_lista):
    return len(auto_lista)


def legfiatalabb_auto(auto_lista):
    i = 1
    maximum = 0
    while i < len(auto_lista):
        if auto_lista[i].gyartasi_datum > auto_lista[maximum].gyartasi_datum:
            maximum = i

        i += 1

    return auto_lista[maximum]

def legoregebb_auto(auto_lista):
    i = 1
    minimum = 0

    while i < len(auto_lista):
        if auto_lista[i].gyartasi_datum < auto_lista[minimum].gyartasi_datum:
            minimum = i

        i += 1

    return auto_lista[minimum]
