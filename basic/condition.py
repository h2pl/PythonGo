age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')






names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)



names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
s = set([1, 2, 3])

ss = set([1, 1, 2, 2, 3, 3])
print(ss)