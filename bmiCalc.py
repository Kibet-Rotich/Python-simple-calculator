#ASBEL KIBET ROTICH
#SCT211-0087/2022
# Input from the user
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
else:
    category = "Overweight"

# Display the BMI and category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are {category}.")
