'''Tracking BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more
Lets try it !!!!'''

weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the weight in centimeters: "))
height = height/100
BMI = weight/(height)**2
print(f"Height: {height} meters")
print(f"Weight: {weight} kg")
print(f"Your BMI is {BMI: .2f}")

if (BMI < 18.5):
    print("Considering your BMI, you seem to be Underweight.")
elif (BMI>=18.5 and BMI<25):
    print("Considering your BMI, you seem to be Healthy.")
elif (BMI>=25 and BMI<30):
    print("Considering your BMI, you seem to be Overweight.")
else:
    print("Considering your BMI, you seem to be severely Overweight.")
