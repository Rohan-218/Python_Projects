# file = open("file.txt", mode = "r")
try:
    with open("file.txt", mode = "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("Error:" + str(e))

# file.close()

with open("file.txt", "a") as file:
    file.writelines(["This is a new file created using python", 
                     "\nThis is the second line", 
                     "\nThis is the third line"
                    ])
    

import re

# Open the file that you have saved in your folder
handle = open('file.txt')
data = handle.read()

# Find all the numbers in the text
numbers = re.findall('[0-9]+', data)

# Convert strings to integers and calculate the total sum
total = sum([int(n) for n in numbers])

print(total)
