numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()


for i in numbers:
    if i == 1:
        continue

    for j in range(2, i):
        is_primes = (i % j) != 0
        if is_primes == True:
            primes.append(i)
            break
        else:
            not_primes.append(i)
            break
print(f'Primes = {primes}\nNot Primes = {not_primes}')