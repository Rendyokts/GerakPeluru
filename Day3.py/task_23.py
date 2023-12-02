for i in range(1, 6):
    for j in range(1, 6):
        if j == 1:
            print(i, end=' ')
        if j == 2:
            print(1, end=' ')
        if j == 3:
            print(i, end=' ')
        if j == 4:
            print(i**2, end=' ')
        if j == 5:
            print(i**3, end=' ')
    print()