#1
family_members = ('Aldo', 'Rafli', 'Suryono', 'Mimin')
brother1, brother2, *parents = family_members

print(brother1)
print(brother2)
print(parents)

#2
fruits = ('Anggur', 5, 'Jeruk')
veggie = ('Sawi', 'Kangkung', 'Bayam')
beef = ('Sosis', 'Nugget', 'Sarden')
food_stuff_tp = fruits + veggie + beef
print(food_stuff_tp)


#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

food_stuff_lt[2] = 'Agus'
print(food_stuff_lt) 

#4
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index -1:middle_index +2]
print(middle_items)

#5
print(food_stuff_lt[:3])

#6
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
