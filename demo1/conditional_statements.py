try:
    age = int(input("Enter Age: "))

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

except ValueError:
    print("Please enter a valid number")