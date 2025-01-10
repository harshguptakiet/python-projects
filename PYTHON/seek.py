with open("example.txt","r") as file:
     file.seek(5)
     print("After seeking to 5th byte:",file.read(5))

     file.seek(5,0)
     
     print("After seeking to 5th byte:",file.read(5))

     