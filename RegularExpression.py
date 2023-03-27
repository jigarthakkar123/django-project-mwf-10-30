import re
 
'''
s = 'GeeksforGeeks: A computer science portal for geeks'
 
match = re.search(r'portal', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())

s = 'geeks.forgeeks'
 
# without using \
match = re.search(r'.', s)
print(match)
 
# using \
match = re.search(r'\.', s)
print(match)
'''

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
 
print(result)
