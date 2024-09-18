calls = 0
def count_calls ():
     global calls
     calls = calls + 1
def string_info (a):
    count_calls()
    b = len(a)
    a = (b, a.upper(), a.lower())
    return(a)
def is_contains(stroka, list_):
    count_calls()
    stroka = str(stroka).lower()
    list_ = list(list_)
    for i in range(len(list_)):
        if str(list_[i]).lower() == stroka:
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)












