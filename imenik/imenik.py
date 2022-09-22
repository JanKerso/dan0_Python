imenik = {"Ana":9684198, "Maja": 9874169, "Ema":89416984, "Miha":6876987, "Tilen":65419, "Aljaz":6854984, "Andrej":65410654, "Anastazija":321365, "Andraz":567464}

ime_za_klic = [(ime, st) for ime, st in imenik.items() if ime[0:] == "A"]

for ime, st in ime_za_klic:
    print("Klicem " + ime + " na tel st. " + str(st))

