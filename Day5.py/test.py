# list built in functions
lst = list()
empty_list = list() # empty list of functions
print(len(empty_list))

# using square brackets
lst = []
empty_list = [] # empty list of functions
print(len(empty_list))

# list with initial values. We use len() to find the lenght of a list
fruits = ['banana', 'orange', 'mango', 'lemon'] # list of fruits
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot'] # list of vegetables for
animal_products = ['milk', 'meat', 'butter', 'yoghurt'] # list of animal products
web_tech = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB'] # list of web tech
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # list of countries

print('Fruits                   :',fruits)
print('Number of fruits         :',len(fruits))
print('Vegetables               :',vegetables)
print('Number of vegetables     :',len(vegetables))
print('Animal products          :',animal_products)
print('Number of animal products:',len(animal_products))
print('Web tech                 :',web_tech)
print('Number of web tech       :',len(web_tech))
print('Countries                :',countries)
print('Number of countries      :',len(countries))
print('=========================')

# list can have items of different data types
lst = ['Rendi Oktavian', 'True', {'country:''Indonesia', 'city:''Jakarta'}]
print(lst)

# accessing list items using negative indexing
print('=========================')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('-4 is the first fruit:',fruits[-4])
print('-1 is the last fruit:',fruits[-1])
print('-2 is the second last fruit:',fruits[-2])

# Unpacking list items
print('=========================')
item = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = item
print(first_item) #item 1
print(second_item)  #item 2
print(third_item)   #item 3
print(rest) #sisa item  

print('======First Example======')
buah = ['banana', 'orange','mango', 'lemon', 'lime', 'apple']
first_buah, second_buah, third_buah, *rest = buah
print(first_buah) #banana
print(second_buah)  #orange
print(third_buah)   #mango
print(rest) #sisa item

print('======Second Example======')
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first) #1
print(second) #2
print(third) #3
print(rest) #sisa item
print(tenth) #10

print('======Third Example======')
negara = ['Jerman', 'Perancis', 'Belgia', 'Swedia', 'Denmark', 'Finlandia', 'Norwegia', 'Islandia','Estonia']
jr, pr, sw, *scandic, es = negara
print(jr) #Jerman
print(pr) #Perancis
print(sw) #Swedia
print(scandic) #sisa item
print(es) #Estonia

print('=Slicing items from a list=')
# positive indexing
buah = ['banana', 'orange', 'mango','lemon']
semua_buah = fruits[0:4] # it returns all the fruits
print(semua_buah) #['banana', 'orange','mango', 'lemon']
semua_buah = fruits[0:] #jika tidak mengatur index maka akan mengeluarkan semuanya
print(semua_buah)
semua_buah = fruits[:2] # jika indexnya mengandung indexnya maka akan mengeluarkan semuanya
print(semua_buah)

print('=Slicing items form a list=')
# negative indexing
buah = ['banana', 'orange','mango','lemon']
semua_buah = fruits[-4:] # it returns all the fruits
print(semua_buah) #['banana', 'orange','mango', 'lemon']
semua_buah = fruits[-1:] #jika tidak mengatur index maka akan mengeluarkan semuanya
print(semua_buah)
semua_buah = fruits[-2:] # jika indexnya mengandung indexnya maka akan mengeluarkan semuanya
print(semua_buah)

# modifying list
print('======Modifying list======')
fruits = ['banana', 'orange','mango', 'lemon']
print(fruits)
fruits[0] = 'avocado'
print(fruits) # mengganti index pertama dengan yang baru dimasukkan sesuai dengan nomer index
fruits[1] = 'apple'
print(fruits) # mengganti index kedua dengan yang baru dimasukkan sesuai dengan nomer index
last_index = len(fruits) - 1 
fruits[last_index] = 'lime'
print(fruits) # mengganti index terakhir dengan yang baru dimasukkan sesuai dengan nomer index

print('=adding items to a list=')
# method append()
lst = list()
lst.append(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)

print('=inserting items into a list=')
# method insert()
lst = ['item1', 'item2']
#lst.insert(index, item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)
fruits.insert(3, 'pinneapple') # inserting pinneapple
print(fruits)

print('=removing items from a list=')
# method remove()
lst = ['item1', 'item2']
lst.remove('item1')

fruits = ['banana', 'orange','mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

print('=Removing items using pop=')
# method pop()
lst = ['item1', 'item2']
lst.pop() # remove last item if not indexing
#lst.pop(index)

fruits = ['banana', 'orange','mango', 'lemon']
fruits.pop()
print(lst)

fruits.pop(0)
print(fruits) # remove the first index

print('=Removing items using Del=')
# method del()
lst = ['item1', 'item2']
#del lst[index] # only a single item
del lst # to delete list completely

fruits = ['banana', 'orange','mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits) # menghapus index pertama

del fruits[1]
print(fruits)

del fruits[1:3] # delete items between given indexes
print(fruits)

#del fruits
#print(fruits) # akan menampilkan error karna harus memasukan index

print('=Clearing list items=')
# method clear() empties the list
lst = ['item1', 'item2', 'item3']
lst.clear()

fruits = ['banana', 'orange','mango', 'lemon']
fruits.clear() # this index will remove all the items
print(fruits)

print('=Copying a list=')
# method copy()
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. 
# Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. 
# But there are lots of cases in which we do not like to modify the original instead we like to have a different copy. 
# One way of avoiding the problem above is using copy().
lst = ['item1', 'item2']
lst_copy = lst.copy()

fruits = ['banana', 'orange','mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

print('=Joining a list=')
# method Plus Operator (+)
#lst3 = list1 + list2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-1, -2, -3, -4, -5]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot']
fruit_and_vegetables = fruits + vegetables
print(fruit_and_vegetables)

print('=Joining using extend=')
# method extend() allows to append list in a list
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6, 7]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2,-1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Numbers:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:',fruits)

print('=Counting items list=')
# method count()
lst = ['item1', 'item2']
lst.count(item)

fruits = ['banana', 'orange','mango', 'lemon']
print(fruits.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count('24'))

print('=Finding index of an item=')
# method index()
lst = ['item1', 'item2']
#lst.index(item)

fruits = ['banana', 'orange','mango', 'lemon']
print(fruits.index('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

print('=Reversing a list=')

# method reverse() reverses the order of a list
lst = ['item1', 'item2']
lst.reverse()

fruits = ['banana', 'orange','mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

print('=Sorting a list=')
# method sort() To sort lists we can use sort() method or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list. 
# If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
lst = ['item1', 'item2']
lst.sort() # ascending order = naik
lst.sort(reverse=True) # descending order = turun

fruits = ['banana', 'orange','mango', 'lemon']
fruits.sort() # mengurutkan sesuai alphabet
print(fruits)

fruits.sort(reverse=True) # mengurutkan kebalikannya sesuai alphabet
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort() # mengurutkan dari angka terkecil
print(ages)

ages.sort(reverse=True) # mengurutkan kebalikannya dari angka terkecil
print(ages)

print('=Sorted=')
# method sorted() returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))

fruits = ['banana', 'orange','mango', 'lemon']
fruits = sorted(fruits,reverse = True)
print(fruits)