

calls = 0

def count_calls():
    global calls
    calls += 1
def string_info():
    string = input('Введите слово: ')
    tuple_ = tuple((len(string), string.upper(), string.lower()))
    print(tuple_)
    count_calls()
def is_contains():
    string = input('Введите слово: ').lower()
    list_to_serch = [input('Введите слово: ').lower()]
    for i in list_to_serch:
        if string in i:

            break

        else:
            print(False)
    count_calls()

string_info()
string_info()
is_contains()
is_contains()
print(calls)

"""
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
"""
