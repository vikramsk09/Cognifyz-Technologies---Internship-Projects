temp = int(input("Enter the temperature: "))
current_unit = input("Enter the current temperature unit (C/F): ").lower()

if current_unit == "c":
    F = (temp * 9/5) + 32
    print(f"{temp}° C = {round(F, 2)}° F")

elif current_unit == "f":
    C = (temp - 32) * 5/9
    print(f"{temp}° F = {round(C, 2)}° C")

