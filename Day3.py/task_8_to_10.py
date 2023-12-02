# Mencari slope dan interception
m = 2
b = -2

x_intercept = -b / m
y_intercept = b

print("Kemiringan (slope): ",m)
print("x-intercept: ",x_intercept)
print("y-intercept: ",y_intercept)

# Mencari slope dan Euclidean distance
# (m = y2-y1/x2-x1) Point (2, 2) and (6, 10)

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1, y1 = 2, 2
x2, y2 = 6, 10

k = slope(x1, y1, x2, y2)
l = distance(x1, y1, x2, y2)

print("slope: ", m)
print("distance: ", l)

compare = m - k
print("compare: ", compare)
