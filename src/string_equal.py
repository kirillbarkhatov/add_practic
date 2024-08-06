def string_equal(strings: list) -> list:

    return [i for i in [j for j in strings if j != ""] if i[0] == i[-1]]


test1 = ['hello', 'world', 'apple', 'pear', 'banana', 'pop']
test2 = ['', 'madam', 'racecar', 'noon', 'level', '']
test3 = []

print(string_equal(test1))
print(string_equal(test2))
print(string_equal(test3))