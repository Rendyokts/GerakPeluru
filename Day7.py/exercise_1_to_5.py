it_companies = {'facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon'}
A = {19, 22, 24 , 20, 25, 26}
B = {'19', 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
print(len(B))

#2
it_companies.add('twitter')
print(it_companies)

#3
it_companies.update({'Thinkpad', 'Meta', 'SpaceX'})
print(it_companies)

#4
it_companies.pop()
print(it_companies)

#5
it_companies.discard('facebook')
print(it_companies)

it_companies.remove('twitter')
print(it_companies)

# U = {1,2,3,4,5,6,6,7,8,9,10}
# A = {1,4,7,10}
# B = {1,2,3,4,5}
# C = {2,4,6,8}

# print(B.intersection(C))#a
# print(A.difference(B))
# print(A.symmetric_difference(U))
# print(U.difference(C))
# print(B.intersection(U))
# print(A.intersection(B.union(C)))
# print((A.union(B)).difference(C))
# print(A.intersection(B).union(C))

# import itertools
# X = {1,2}
# Y = {'a', 'b', 'c'}

# itertools.product(X,X,X)
# print(list(itertools.product(X,X,X)))
