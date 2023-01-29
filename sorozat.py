import random


def lottoszam_generator():
    lista = []
    i = 0
    while i < 5:
        vel = random.randint(1, 99)
        lista.append(vel)
        i += 1

    return lista


def lottoszam_kiirato(lista):
    i = 0
    szoveg = ""
    while i < len(lista):
        szoveg += f"{lista[i]}{';' if (i < len(lista) - 1) else ''}"
        i += 1

    print(f"II/A, B, C:\n\t{szoveg}")


def egyjegyuek_szama(lista):
    i = 0
    db = 0
    while i < len(lista):
        if 1 <= lista[i] <= 9:
            db += 1
        i += 1

    return db

def konzol_kiir(szam):
    print(f"II/D, E:\n\tAz egyjegyűek száma: {szam}.")

def file_kiir(szam):
    f = open("szamok.txt", "w", encoding="utf-8")
    f.write(f"II/F:\n\tAz egyjegyűek száma: {szam}.")
    f.close()