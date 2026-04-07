with open("test.txt", "w") as f:
    f.write("Hello Python")
    f.write("\nHello Uday")

with open("test.txt", "r") as f:
    print(f.read())

'''
Hello Python
Hello Uday
'''