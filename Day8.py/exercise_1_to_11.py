#1
dog = {}

#2
dog = {
    'Name': 'Trixie',
    'Color': 'Golden',
    'Breed': 'Golden Retrievers',
    'Legs': 'Strong',
    'age': '2'
}

#3
student = {
    'first_name': 'Agus',
    'last_name': 'Mulyadi',
    'gender': 'Male',
    'age': 18,
    'isMarried': False,
    'Skills': 'Mancing',
    'Country': 'United States',
    'City': 'Orange County',
    'Address': {
        'Street': 'Raya Bogor',
        'PostalCode': '19651'
    }
}

#4
print(len(student))

#5
print(student['Skills'])

#6
student['Skills'] += ', Games, Sleeping' #to add values 1 or 2 into the key
print(student)

#7
print(dog.keys())

#8
print(dog.values())

#9
print(student.items())

#10
del student['Skills']
print(student)

#11
del student
print(student)