row = int(input("Enter number of rows: "))  

#for i in reversed(range(1, row)):  
for i in range(row, 0, -1):  
    # Print spaces  
    for j in range(row - i): #nested loop used  
        print("  ", end="")  
      
    # Print stars  
    for stars in range(2 * i - 1):  
        print("* ", end="")  
      
    print()     