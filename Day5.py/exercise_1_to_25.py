# number 1
lst = ()
# number 2
lst = ['pagi', 'siang', 'sore', 'malam', 'dini hari']
# number 3
length = len(lst)
print(length)
# number 4
print('The first item is:', lst[0])

middle_index = (length - 1)//2 # untuk mencari index yang berada ditengah
print(middle_index)
print('The middle item is:', lst[2])
print('The last item is:', lst[-1]) # -1 selalu menampilkan hasil index akhir

# number 5
mixed_data_types =['Rendi Oktavian', '26', '180','Married','City:''Jakarta']

# number 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Amazon']

# number 7
print()

# number 8
print(len(it_companies))

# number 9
print('The first company in the list is:',it_companies[0])
middle_company = (len(it_companies) -1)//2
print(middle_company)
print('The middle company in the list is:',it_companies[2])
print('The last company in the list is:',it_companies[-1])

# number 10
it_companies[0] = 'Twitter'
print(it_companies)

# number 11
it_companies.append('IT company')
print(it_companies)

# number 12
print('Nomer 12')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Amazon']
print(it_companies)
index = (len(it_companies) -1) // 2
it_companies.insert(index, 'IT company')
print(it_companies)

# number 13
print('Nomer 13')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
print('Make it uppercase:' ,it_companies[2].upper())

# number 14
print('# '.join(it_companies))

# number 15 to check a certain company in the list
#company = input('Masukkan salah satu dari IT Company:')
#if company in it_companies:
    #print(f'{company} exists in the list of IT Company')
#else:
    #print(f'{company} does not exist in the list of IT Company')

# number 16
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
it_companies.sort()
print(it_companies)

# number 17
it_companies.sort(reverse=True)
print(it_companies)

# number 18
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
perusahaan = it_companies[:3] # slice out the first three companies
print(perusahaan)

# number 19
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
perusahaan = it_companies[3:] # slice out the last three companies
print(perusahaan)

# number 20
print('=Nomer 20=')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
length = len(it_companies)
print(length)
middle_company = ((length) -1)// 2
print(middle_company)
middle_company = (it_companies[2])
print(middle_company)

# number 21
it_companies.pop(0) # it will remove the index by number indexing
print(it_companies)

# number 22
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
it_companies.pop(2)
print(it_companies)

# number 23
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
it_companies.pop(-1)
print(it_companies)

# number 24
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
it_companies.clear()
print(it_companies)

# number 25
it_companies_copy = it_companies[:]
del it_companies