count = 0;
while count < 5:
    print(count)
    count = count + 1
    if count == 5:
        break

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':25,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', + number + 1 ) if number !=5 else print("loop's end")
print('Outside the loop')

for number in range(0,11,1): # range(start, end, step)
    print(number)

for key in person:
    if key == 'skills':
        for skill in person:
            print(skill)

for number in range(0,11,3):
    print(number)
else:
    print('The loop stops at', number)

for number in range(6):
    pass