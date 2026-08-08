# read
fx = open("sample.txt", "r") 
data = fx.read()
print(data)

# write
f = open("sample.txt", "rt")

f.write("Hello! Myself Shruti and completing python course")
f.close()

# append
x1 = open("sample.txt", "a")
x1.write(" \nHelpful in upgrading my skills")

# create a new txt file
x2 = open("sample2.txt", "x")
x2.write("This is a new file")
f.close()

