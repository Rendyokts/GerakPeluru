it_companies = {'facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon'}
A = {19, 22, 24 , 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age = set(age)
print(len(age))
print(max(age))
print(age)

#2
#String adalah tipe data yang digunakan untuk mempresentasikan teks atau urutan karakter
#list adalah struktur data yang dapat menampung koleksi elemen, dapat diubah dan berisi elemen dengan tipe data yang berbeda, list ditandai dengan []
#tuple adalah struktur data yang dapat menampung koleksi elemen, tidak dapat diubah dan berisi elemen dengan tipe data yang sama, tuple ditandai dengan ()
#set adalah struktur data yang dapat menampung kumpulan elemen unik, tidak beraturan, dan tidak dapat menyimpan 2 elemen yang sama, ditandai dengan {}

#3
words = 'i am a teacher and i love to inspire and teach people'
text = words.split()
unique_words = set(text)
print(unique_words)