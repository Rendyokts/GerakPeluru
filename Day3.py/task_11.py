#calculate the value of y(y = x^2 + 6x + 9)

def equation(x):
    y = x**2 + 6*x + 9
    return y

x1 = 3
y1 = equation(x1)
print("When x = {}, y = {}".format(x1, y1))

x2 = -2
y2 = equation(x2)
print("When x = {}, y = {}".format(x2, y2))

x3 = 0
y3 = equation(x3)
print("When x = {}, y = {}".format(x3, y3))

x4 = -3
y4 = equation(x4)
print("When x = {}, y = {}".format(x4, y4))