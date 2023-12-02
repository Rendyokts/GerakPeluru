it_companies = {'facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon'}
A = {19, 22, 24 , 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(A.union(B))

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

#7
del A
del B
print(A)