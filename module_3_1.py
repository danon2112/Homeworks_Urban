calls = 0

def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    is_contains_flag = False
    for stroka in list_to_search:
        if stroka.lower() == string.lower():
            is_contains_flag = True
            break
    return is_contains_flag

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)