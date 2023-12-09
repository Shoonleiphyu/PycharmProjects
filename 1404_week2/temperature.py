def main():
    Menu= """C= Celsius to Fahrenheit
F= Fahrenheit to Celsius
Q= Quit"""
    print(Menu)
    choice = input("Enter your choice: ").upper()
    while choice!="Q":

        if choice=="C":
            celsius = float(input("Celsius: "))
            fahrenheit = temp_fah(celsius)
            print(f"Result is {fahrenheit: .2f} F")

        elif choice=="F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = temp_cel(fahrenheit)
            print(f"Result is {celsius: .2f} C")

        else:
            print("invalid option")

        print(Menu)
        choice = input("Enter your choice: ").upper()

    print("Thank you")

def temp_fah(celsius):
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit
def temp_cel(fahrenheit):
        celsius = 5 / 9 * (fahrenheit - 32)
        return celsius



main()







