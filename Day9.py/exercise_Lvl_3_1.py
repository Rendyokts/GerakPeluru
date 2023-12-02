person = {
    'first_name': 'Rendi',
    'last_name': 'Oktavian',
    'age': 27,
    'country': 'Indonesia',
    'isMarried': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    if len(skills) >= 3:
        middle_skill = skills[len(skills)//2]
        print(f"middle skill : {middle_skill}") 

if 'skills' in person:
    has_py_skill = 'Python' in person['skills']
    print(f"has_py_skill : {has_py_skill}") 

if 'skills' in person:
    skills_set = set(person['skills'])

    if skills_set == {'Javascript', 'React'}:
        print('He is a front end developer')
    elif skills_set == {'Node', 'Python', 'MongoDB'}:
        print('He is a back end developer')
    elif skills_set == {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

if person.get('isMarried') and person.get('country') == 'Finland':
    print(f"{person['first_name']}: {person['last_name']} is married and lives in Finland. Address: {person['address']['street']}, {person['address']['zipcode']}")