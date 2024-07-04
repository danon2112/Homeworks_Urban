def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return
print_params(12, 10, False)
print_params(0, 22)
print_params()
print_params(b = 25)  # Работает
print_params(c = [1,2,3]) # Работает

print('\n===================\n')

values_list = ['string', False, 123]
values_dict = {
    'a': 'Daniil',
    'c': 'Urban',
    'b': 2024
}
print_params(*values_list)
print_params(**values_dict)

print('\n===================\n')

values_list_2 = ['string', 123]
print_params(*values_list_2, 42)