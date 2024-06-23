immutable_var = ("Daniil", 17, True)
print(immutable_var)

# immutable_var[1] = 18
# print(immutable_var)
# На этом этапе программа выдаст ошибку. К кортежу можно только обращаться по индексу (в кортеже неизменяемы элементы), но не менять значения. Для этих целей подойдёт список!

mutable_list = ['Moscow', 'Omsk', 'Novgorod', 'Tver']
mutable_list[1] = 'Smolensk'
print(mutable_list)