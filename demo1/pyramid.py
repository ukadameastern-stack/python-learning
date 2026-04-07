row = int(input("Enter number of rows: "))  
  
for i in range(1, row + 1):  
    # Print spaces  
    for j in range(row - i): #nested loop used  
        print("  ", end="")  
      
    # Print stars  
    for stars in range(2 * i - 1):  
        print("* ", end="")  
      
    print() 