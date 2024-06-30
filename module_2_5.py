def get_matix(n, m, value):
    matrix = list()
    for i in range(n):
        matrix.append(list())
        for j in range(m):
            matrix[i].append(value)
    return matrix
resault = get_matix(2, 2, 10)
print(resault)