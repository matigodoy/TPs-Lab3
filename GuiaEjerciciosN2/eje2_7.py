def capicua(palabra: str):
    if palabra == palabra[::-1]:
        print(f"La palabra {palabra} es capicua")
    else:
        print(f"La palabra {palabra} no es capicua")

capicua("holabro")
capicua("neuquen")