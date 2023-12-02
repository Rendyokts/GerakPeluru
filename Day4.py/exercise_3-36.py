# number 3
company = 'Coding For All'
# number 4
print('the result                 : ',company)
# number 5
length = len(company)
print('the length                 : ',length)
# number 6

print('uppercase                  : ',company.upper())
# number 7
print('lowercase                  : ',company.lower())
# number 8
print('capitalized                : ',company.capitalize())
print('title                      : ',company.title())
print('swapcase                   : ',company.swapcase())
# number 9
print('cutting the Coding         : ',company[:6])
# number 10
print('check index                : ',company.index('Coding'))
print('chech rindex               : ',company.rindex('Coding'))
# number 11
print('replace words              : ',company.replace('Coding','Python'))
# number 12
company = 'Python For All'
print('replace words              : ',company.replace('Python For All','Python For Everyone'))
# number 13
print('split words                : ',company.split())
# number 14
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print('split words                : ',companies.split(','))
# number 15
company = 'Coding For All'
index_0 = company[0]
print('first character            : ',index_0)
# number 16
index_minus1 = company[-1]
print('last character             : ',index_minus1)
# number 17
find_index = company[9]
print('find index                 : ',find_index)
# number 18
company = 'Python for everyone'
words = company.split()
print('acronym                    : ',"".join(word[0] for word in words))
# number 19
company = 'Coding for all'
words = company.split()
print('acronym                    : ',"".join(word[0] for word in words))
# number 20
print('positions                  : ',company.index("C"))
# number 21
print('positions                  : ',company.index("f"))
# number 22
print('rfind                      : ',company.index('l'))
# number 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
find_index = sentence.index('because')
print('index of the first occ     : ',find_index)
# number 24
find_index = sentence.rindex('because')
print('index of the last occ      : ',find_index)
# number 25
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print('cutting                    : ',sentence[start:end])

# number 28
company = 'Coding For All'
if company.startswith('Coding'):
    print(company,', The string starts with Coding')
else:
    print(company,', The string does not start with Coding')

# number 29
if company.endswith('Coding'):
    print(company,', The string ends with Coding')
else:
    print(company,', The string does not end with Coding')

# number 30
company = '  Coding For All  '
print('remove the spaces          :',company.strip())

# number 31
print('===========================')
company_1 = '30DaysOfPython'
company_2 = 'thirty_days_of_python'

print(company_1.isidentifier())
print(company_2.isidentifier())

# number 32
print('===========================')
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libraries))

# number 33
print('===========================')
sentences = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentences)

# number 34
print('===========================')
print('Name\tAge\tCountry\tCity')
print('Rendi\t26\tIndo\tJakarta')
print('Kinanti\t1\tEng\tEdinburgh')

# number 35
print('===========================')
radius = 10
area = 3.14 * radius ** 2
formated_string = 'the area of a circle with radius %d is %.2f.' %(radius, area)
print(formated_string)

# number 36
print('===========================')
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))