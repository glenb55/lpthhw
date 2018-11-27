from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C),")
print("If you want to do that, hit RETURN.")

input ("?")

print("Opening the file...")
target = open(filename ,'w')

target("Trincating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you fro three lines.")

line1 = input ("line1: ")
line2 = input ("Line2: ")
line3 = input ("Line3: ")

print("I'm goint to write these to the file.")

target.write(line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.write(Line3)
target.write("\n")

print("And finally, we close it.")
target.close
