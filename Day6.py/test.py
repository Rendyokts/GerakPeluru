# empty_tuple = ()
# empty_tupple = tupple()

tpl = ('item1', 'item2', 'item3')
#Positif indexes
all_items = tpl[0:3] #print all index items
print(all_items)
all_items = tpl[1:3] #not included the 1st index
print(all_items)
all_items = tpl[2:3] #not included the 1st and 2nd index
print(all_items)
all_items = tpl[3:3] #not included the all index
print(all_items)

#Negative index
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:] #print all index items
print(all_fruits)
all_fruits = fruits[-3:-1] #doesnt include item at index 3 and 1 
print(all_fruits)
all_fruits = fruits[-3:] #doesnt include item at index 1 
print(all_fruits)

#Changing Tuples to List
tpl = ('items1', 'items2', 'items3','items4')
lst = list(tpl)
print(lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple' #Change the 1st index
print(fruits)

fruits = tuple(fruits)
print(fruits)

#Checking an item in a Tuple
tpl = ('items1', 'items2', 'items3', 'items4')
print('items2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
fruits= list(fruits)
# fruits[0] = 'apple'
# print(fruits)
print('apple' in fruits)

#Joining tuples
tpl1 = ('items1', 'items2', 'items3', 'items4')
tpl2 = ('items5', 'items6', 'items7')
tpl3 = tpl1 + tpl2
print(tpl3)
print('items8' in tpl3)

#Deleting tuples
tpl1 = ('items1', 'items2', 'items3', 'items4')
del tpl1
print(tpl1)