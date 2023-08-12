COLOR_TO_HEX = {"Absolutezero": "#0048ba", "Acidgreen": "#b0bf1a", "Aliceblue": "#f0f8ff", "Alizarincrismon": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antiquewhite": "#faebd7",
                "Antiquewhite1": "#ffefdb", "Antiquewhite2": "#eedfcc"}
print(COLOR_TO_HEX)

for color_name, color_code in COLOR_TO_HEX.items():
    print(f"{color_name} is {color_code}")

color_name = input("Enter a color: ")

while color_name != "":
    try:
        color_code = COLOR_TO_HEX[color_name.capitalize()]
        print(f"{color_name} is {color_code}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color: ")
