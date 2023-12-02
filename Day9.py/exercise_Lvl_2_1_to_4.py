#1
scores = int(input("Student scores: "))

if scores >= 80:
    grade = 'A'
elif scores >= 70:
    grade = 'B'
elif scores >= 60:
    grade = 'C'
elif scores >= 50:
    grade = 'D'
else:
    grade = 'E'
print(grade)

#2
Months = input("Enter Month: ")

if Months.lower() in ['september', 'october', 'november']:
    print("The season is Autumn")
elif Months.lower() in ['december', 'january', 'february']:
    print("The season is Winter")
elif Months.lower() in ['June', 'July', 'August']:
    print("The season is Summer")
else:
    print("The season is Spring")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruits = 'watermelon'

if add_fruits in fruits:
    print("The fruit already exist in the list")
else:
    fruits.append(add_fruits)
    print(fruits)
