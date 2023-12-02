st = {'item1', 'item2', 'item3'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

st.add('item5') #menambahkan 1 elemen
print(st)

st.update(['item4', 'item6']) #Menambahkan lebih dari 1 elemen
print(st)

fruits.update(st) #bisa juga menambahkan seperti ini dengan menambil elemen pada variable set lain
print(fruits)

st.remove('item1') #menghapus elemen pada set
print(st)

st.pop() #menghapus satu elemen secara random
print(st)

removed_item = st.pop() #jika ingin melihat elemen mana yang dihapus
print(removed_item)
print(st)

st.clear() #menghapus variable dan menjadikannya set kosong
print(st)

del st #untuk menhapus variable dan seluruh isi elemen

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
st = set(lst) #convert to list
print(st) #output nya akan random, karena himpunan secara umum tidak terurut

st1 = {'item1', 'item2', 'item3'}
st2 = {'item2', 'item3'}
print(st1.union(st2)) #Menggabungkan set 

print(st2.intersection(st1)) #Mencari item persimpangan, atau 1 item yang memiliki nilai yang sama

print(st2.issubset(st1))
print(st1.issubset(st2))
print(st1.issuperset(st2))
print(st2.issuperset(st1))

print(st2.difference(st1)) #mencari perbedaan pada tiap set
print(st1.difference(st2))

print(st2.symmetric_difference(st1)) #mencari perbedaan
print(st1.symmetric_difference(st2)) #mencari perbedaan

print(st2.isdisjoint(st1)) #mencek penggabungkan set
