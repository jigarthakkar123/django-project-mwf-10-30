str1 = 'Tops Technologies'

rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))


def cube(y):
    return y*y*y
 
 
lambda_cube = lambda y: y*y*y

print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))
