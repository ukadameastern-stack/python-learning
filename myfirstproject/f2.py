with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
  f.write("\nFile line 1.")
  f.write("\nFile line 2.")
  f.write("\nFile line 3.")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())