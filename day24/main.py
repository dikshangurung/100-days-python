with open("my_file.txt",mode="r") as file:
    # file.write("This is where I ,I draw the lines I can no longer change")
    print(file.read())

with open("my_file.txt",mode="a") as file2:
    file2.write("\n OK cha ta")

