# here we have to close the file 
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# another way to open a file is, here we don't have to close the file
with open("my_file.txt", mode="w") as file:
    # contents = file.read()
    file.write("Prithwish Dey")
    # print(contents)