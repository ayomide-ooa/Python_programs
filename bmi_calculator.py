#BMI Calculator
#formulae: BMI = kg/m²
height, weight = float(input("Input your height in meters (m): ")), float(input("Input your weight in kilograms (kg): "))

bmi = round(weight/(height**2), 1)

print("your Body Max Index is ",bmi )