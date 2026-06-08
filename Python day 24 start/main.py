with open("/Users/Halima/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# if you want to read from the file


with open("my_file.txt", mode = "w") as file:
     file.write("New_text")

with open("new_file.txt", mode = "w") as file:
     file.write()