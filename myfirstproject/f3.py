# Overwrite Existing Content

with open("demofile2.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
  f.close()

#open and read the file after the overwriting:
with open("demofile2.txt") as f:
  print(f.read())
  f.close()