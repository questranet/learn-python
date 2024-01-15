import os

name = os.environ['HOME']
print(name)



# To create a file using Python OS module
with open('/tmp/1.txt', 'w') as file:
    file.write('This is an example file .\n')
    file.write('It was created using the os module in Python')

