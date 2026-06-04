# file = open("file.txt", mode = "r")
try:
    with open("file.txt", mode = "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("Error:" + str(e))

# file.close()

with open("file.txt", "w") as file:
    file.writelines(["This is a new file created using python", 
                     "\nThis is the second line", 
                     "\nThis is the third line"
                    ])