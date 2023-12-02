empty_dict = {}
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
print(dct.values())
print(dct.keys())

person = {
    'first_name' : 'Rendi',
    'last_name' : 'Oktavian',
    'age' : 27,
    'is_married' : True,
    'country' : 'Indonesia',
    'skills' : ['Javascript', 'Python', 'Mysql'],
    'address' : {
        'street' : 'Raya bogor',
        'zipcode' : '16951'
    }
}
print(person['first_name'])

dct['key5'] = 'value5' #untuk menambahkan items pada dictionary
print(dct)

person['job'] = 'Programmer'
person['skills'].append('HTML')
print(person)

dct['key1'] = 'value10'
print(dct.values()) #untuk mengubah value yang ada pada key1

dct.popitem() #remove the last item
print(dct)

del person['first_name']
print(person)

print(dct.items()) #mengubah dict menjadi list tuples