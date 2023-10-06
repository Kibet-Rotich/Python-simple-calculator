#ASBEL KIBET ROTICH
#SCT211-0087/2022
# Input from the user
total_bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Check if the tip percentage is valid
if tip_percentage not in [10, 12, 15]:
    print("Invalid tip percentage. Please choose from 10, 12, or 15.")
else:
    # Calculate tip amount
    tip_amount = (total_bill * tip_percentage) / 100
    
    # Calculate total amount per person
    per_person_amount = (total_bill + tip_amount) / num_people
    
    # Display the result rounded to two decimal points
    print(f"Each person should pay: ${per_person_amount:.2f}")
