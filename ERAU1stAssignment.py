numbers = [1, 2, 3, 4, 5]
def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))
names = ['Hotel', 'India', 'Bravo','Yankee','Echo']
def is_name_long(name):
    if len(name) >5:
        return True
    return False
long_names = filter(is_name_long, names)
print(list(long_names))