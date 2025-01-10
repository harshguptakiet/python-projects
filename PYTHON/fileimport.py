import os

if os.path.exists("example.txt"):
    print("file exists")
else:
    print("file does not exist")

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("file does not exist")
if os.path.exists("example.txt"):
    print("file exists")
else:
    os.mkdir("example_directory")
    with open("example.txt","w") as file :
        file.writelines("helloworld!")

        
