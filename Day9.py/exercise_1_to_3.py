#1
age = int(input("Enter your age: "))

if age < 18:
    print("You need" , 18 - age , "years to learn to drive")
else:
    print("You are old enough to learn to drive")

#2 Nested conditions
your_age = int(input("Enter your age: "))
older = your_age - age
younger = age - your_age
if your_age > age:
    print("You are",older, "years older than me")
elif your_age < age:
    print("You are",younger, "years younger than me")
else:
    print("We are in the same age")

#3
a = int(input("Enter numbers of A: "))
b = int(input("Enter numbers of B: "))

if a > b:
    print(a, "is greater than ",b)
elif a < b:
    print(a, "is smaller than ",b)
else:
    print(a, "is equal to ",b)