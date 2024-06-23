my_dict = {
    'Petya': 2000,
    'Masha': 1992,
    'Egor': 1988
}
print(my_dict)
print(my_dict.get('Petya'), my_dict.get('Daniil', 'пустое значение...'))
# или так:
# print(my_dict['Petya'], my_dict.get('Daniil', 'пустое значение...'))
my_dict.update({'Ded': 1976, 'Elena': 2001})
print(my_dict.pop('Masha'))
print(my_dict)

print('\n-------------------------------\n')

my_set = {1, 2, 3, 1, 9, True, False, True, 'Daniil', 'Urban'}
print(my_set)
my_set.update({12, 11, 'Elena'})
my_set.remove(1)
# или можно вот так
# my_set.discard(1) || Такой метод не покажет ошибку, если будет попытка удаления не существующего элемента.
print(my_set)
