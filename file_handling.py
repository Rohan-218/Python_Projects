# file = open("Readme.md", mode = "r")
with open("Readme.md", mode = "r") as file:

    data = file.readline()
    print(data)

# file.close()