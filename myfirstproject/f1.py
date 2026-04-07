fr = open("demofileread.txt", "rt") # FileNotFoundError: [Errno 2] No such file or directory: 'demo.txt'
print('----------Read Complete File----------')
print(fr.read())
fr.close()
# print(fr.read()) # ValueError: I/O operation on closed file.
'''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''

print('----------With Complete File----------')
with open("demofileread.txt") as f:
  print(f.read() +  " .....")

f.close()

'''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck! .....
'''  

print('----------With limited characters----------')

with open("demofileread.txt") as f:
  print(f.read(2))

'''
----------With limited lines----------
He
'''

print('----------Read Line----------')

with open("demofileread.txt") as f:
  print(f.readline())
  print(f.readline())

'''
----------Read Line----------
Hello! Welcome to demofile.txt

This file is for testing purposes.
'''  

print('----------Loop through the file line by line----------')

with open("demofileread.txt") as f:
  for l in f:
    print(l)

'''
----------Loop through the file line by line----------
Hello! Welcome to demofile.txt

This file is for testing purposes.

Good Luck!
'''    