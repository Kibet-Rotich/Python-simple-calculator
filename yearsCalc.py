#ASBEL KIBET ROTICH
#SCT211-0087/2022
# Input from the user
name = input("greetings what is your name?  ")
print("Hi there "+name+",!!! you,ve got a great name.")
dateOfBirth = input("Kindly give me your year of birth:  ")
#year calculaions
years = 2023-int(dateOfBirth)
#month calculations
months = int(years)*12
#days calculations
days = int(years)*365.25
#output
print("Dear,"+name+"you are "+str(years)+" years old")
print("Dear,"+name+"you are "+str(months)+" months old")
print("Dear,"+name+"you are "+str(days)+" days old")