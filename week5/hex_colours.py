COLOR_TO_HEX = {"ABSOLUTEZERO": "#0048ba", "ACIDGREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff", "ALIZARINCRISMON": "#e32636",
                "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc"}
print(COLOR_TO_HEX)

for color_name, color_code in COLOR_TO_HEX.items():
    print(f"{color_name} is {color_code}")

color_name = input("Enter a color: ")

while color_name != "":
    try:
        color_code = COLOR_TO_HEX[color_name.upper()]
        print(f"{color_name} is {color_code}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color: ")
