print('Welcome to the tip calculator')
total_bill = input('What was the total bill?')
percentage = input('What was the percentage would you like to give?')
people_amount = input('How many people to split the bill?')

calculated_percentage = int(percentage)/100
print(calculated_percentage)
per_person_amount = ((float(calculated_percentage) * float(total_bill)) + float(total_bill)) / float(people_amount)

print('Each person should pay: ', per_person_amount)