# String only

first_name = 'Rendi'
last_name = 'Oktavian'
language = 'Python'

formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings and Numbers
radius = 10
pi = 3.14
area = pi * radius **2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flash', 'Numpy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' % (python_libraries)
print(formated_string)


formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

# New string format (str.format)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# String Interpolation / f-Strings

print('======================')

a = 5
b = 2

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


# Unpacking Characters
print('================')
language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing Characters in strings by index
print('================')
language = 'python'
first_letter = language[0]
print(first_letter)

second_letter = language[1]
print(second_letter)

last_index = len(language) - 1
print(last_index)

last_letter = language[last_index]
print(last_letter)

print('================')
last_letter = language[-1]
print(last_letter)

second_last = language[-2]
print(second_last)

# Slicing Python strings
print('================')
first_three = language[0:3]
print(first_three)

last_three = language[3:6]
print(last_three)

last_three = language[-3:]
print(last_three)

last_three = language[3:]
print(last_three)


# Reverse String
print('================')

greeting = 'Hello, world!'
print(greeting[::-1])

# Skipping Characters While Slicing
print('================')
pto = language[0:6:2]
print(pto)

# Capitalize convert the first character to capital letter
print('================')
challenge = 'thirty days of python'
print(challenge.capitalize())

# Count
print('================')
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# Endswith 
print('================')
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# Expandtabs
print('================')
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# Find
print('================')
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.find('x'))

# rfind
print('================')
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

# format
print('================')
first_name = 'Rendi'
last_name = 'Oktavian'
age = 26
job = 'students'
country = 'Indonesia'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence)

radius = 10 
pi = 3.14
area = pi * radius **2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)

# index returns the lowest index of a substring
print('================')
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index(sub_string, 5))

# rindex returns the highest index of a substring
print('================')
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string, 7))

# isalnum checks alphanumeric character
print('================')
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirty days of python 2023'
print(challenge.isalnum())

# isalpha checks if all string element are alphabetic character (a-z and A-Z)
print('================')
challenge = 'thirty days of python'
print(challenge.isalpha())

challenge = 'ThirtyDaysPython'
print(challenge.isalpha())

num = '123'
print(num.isalpha())

# isdecimal checks if all string element are decimal (0-9)
print('================')
challenge = 'thirty days of python'
print(challenge.isdecimal())

challenge = '123'
print(challenge.isdecimal())

challenge = '\u00B2'
print(challenge.isdecimal())

challenge = '12 3'
print(challenge.isdecimal())

# isdigit checks if all string element are digit (0-9 and some other unicode characters for numbers)
print('================')
challenge = 'thirty'
print(challenge.isdigit())

challenge = '30'
print(challenge.isdigit())

challenge = '\u00B2'
print(challenge.isdigit())

# isnumeric checks if all characters in a string are numbers or number related (just like isdigit, just accept more symbols, like ½)
print('================')
challenge = '10'
print(challenge.isnumeric())

challenge = '\u00BD'
print(challenge.isnumeric())

challenge = '10.5'
print(challenge.isnumeric())

# isidentifier checks for a valid identifier - it checks if a string is a valid variable name
print('================')
challenge = '30DaysOfPython'
print(challenge.isidentifier())

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# islower checks if all alphabet characters in the string are lowercase
print('================')
challenge = 'thirty days of python'
print(challenge.islower())

challenge = 'Thirty days python'
print(challenge.islower())

# isupper checks if all upper case characters in the string are uppercase
print('================')
challenge = 'thirty days of python'
print(challenge.isupper())

challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

# join returns a concatenated string
print('================')
web_tech = ['HTML', 'CSS','Javascript','React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS','Javascript','React']
result = '# '.join(web_tech)
print(result)

# strip removes all given characters starting from the beginning and end of the string
print('================')
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))

# replace replace substring with a given string
print('================')
challenge = 'thirty days of python'
print(challenge.replace('python', 'java'))

# split splits the string, using given string or space as separator
print('================')
print(challenge.split())

challenge = 'thirty, days, of, python'
print(challenge.split(', '))

# title returns a title cased string
print('================')
challenge = 'thirty days of python'
print(challenge.title())

# swapcase converts all upper case characters to lower case and all lower case characters to upper case characters
print('================')
challenge = 'thirty days of python'
print(challenge.swapcase())

challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

# startswith checks if string starts with the specified string
print('================')
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = '30 days of python'
print(challenge.startswith('thirty'))