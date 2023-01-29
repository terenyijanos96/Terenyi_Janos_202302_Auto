def bekeres():
    print("I/A:")
    auto_neve = input("\tAutó neve: ")
    auto_gyartasi_datum = int(input("\tGyártási dátum: "))

    if auto_gyartasi_datum == 2022:
        kimenet = "friss gyártás"
    elif auto_gyartasi_datum < 2000:
        kimenet = "öreg autó"
    else:
        kimenet = "Átlagos korú"
    print(f"I/B:\n\tEz az {auto_neve} {kimenet}")
