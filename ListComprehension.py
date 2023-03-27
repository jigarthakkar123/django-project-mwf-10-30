'''
List = [character for character in [1, 2, 3]]
print(List)

list = [i for i in range(11) if i % 2 == 0]
print(list)

numbers = [i*10 for i in range(1, 6)]
print(numbers)
'''
numbers1 = list(map(lambda i: i*10, [i for i in range(1, 6)])) 
print(numbers1)
