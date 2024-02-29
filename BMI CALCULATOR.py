weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = (weight/height**2)
print(BMI)
if BMI < 18.5:
    print("Underweight")
if (BMI >= 18.5) and (BMI < 25):
    print("Normal")
if (BMI >= 25) and (BMI < 30):
    print("Overweight")
if BMI >= 30:
    print("Obesity")
    
    