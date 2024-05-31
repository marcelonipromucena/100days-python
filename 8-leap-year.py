# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
  if year % 100 != 0:
    print('It is a leap year')
  elif year % 400 == 0:
      print('It is a leap year.')
else:
  print('It is not a leap year')