n = int(input('Введите число (3-20): '))
password = str()
if n > 20 or n < 3:
    print(f'Ошибка! Число должно быть от 3 до 20.')
else:
    for i in range(1, n):
        for j in range(i, n):
            if (n % (i + j)) == 0:
                password = f'{password}{i}{j}'

print(password)
