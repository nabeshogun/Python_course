calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    kk = (len(string), string.upper(), string.lower())
    return kk


def is_contains(string, list_to_search):
    count_calls()
    t = True
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            t = True
            break
        else:
            t = False
    return t


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
