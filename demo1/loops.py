print("===For Loop===")
for i in range(1, 7):
    print(i)

print("===While Loop===")    

i = 0
while i < 3:
    print(i)
    i += 1

list = ['uday', 'vijay', 'amol', 'balaji', 'vinod', 'ram']    

for name in list:
    print(name.capitalize())


'''
o/p:

===For Loop===
1
2
3
4
5
6
===While Loop===
0
1
2
===For Loop List===
Uday
Vijay
Amol
Balaji
Vinod
Ram
'''    

for x in "banana":
  print(x)


print(len('uday'))

# taking input from the user  
num = int(input("Enter a Number: "))  
  
# initializing the initial factorial  
fact = 1  
  
# base cases  
if num < 0:  
    # factorial not defined for number less than 0  
    print("Not Defined!")  
elif num == 0 and num == 1:  
    # factorial = 1 for number equal to 0 and 1  
    print(f"{num}! = {fact}")  
else:  
    # using the for loop to iterate from   
    for i in range(2, num + 1):  
        # multiplying the current value with the factorial  
        fact = fact * i  
      
    # printing the factorial of the number  
    print(f"{num}! = {fact}")   

'''
Enter a Number: 5
5! = 120

'''

# given matrix  
matrix_3x3 = [  
    [13, 4, 27],   
    [22, 16, 8],  
    [5, 11, 19]  
    ]  
  
print("Given Matrix:")  
# using nested for loop to iterate through each element of the matrix  
for row in matrix_3x3:  
  for col in row:  
    print(col, end = ' ')  
  print()  