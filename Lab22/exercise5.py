# 5. Create a lambda function as a variable called reverse_string that reverses the given
# string. Create a dictionary of name-value pairs. Use the reverse_string variable to check
# if the name and value pairs are/are not the reverse of each other and print True/False for
# the corresponding key


reverse_string = lambda s: s[::-1]

dictionary = {'name': 'eman', 'hello': 'olleh', 'rat': 'tar', 'python': 'java', 'lecture': 'hall', 'AGATCC': 'CCTGAA'}
for key,val in (dictionary.items()):
    if reverse_string(key)==val:
        print(key,True)
    else:
        print(key,False)