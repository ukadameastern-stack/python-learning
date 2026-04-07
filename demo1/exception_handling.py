try:
    x = int("abc")
except ValueError:
    print("Conversion failed") #Conversion failed


y = int("xyz")
'''
Traceback (most recent call last):
  File "/home/udaysinhkadam/workspace/python_demo/demo1/exception_handling.py", line 7, in <module>
    y = int("xyz")
ValueError: invalid literal for int() with base 10: 'xyz'
'''