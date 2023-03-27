def addition(n):
    return n + n
 
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
 
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)
