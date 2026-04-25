message= input(">")
words=message.split(' ') # LIST IS CREATED
#print(words)
emojis ={
    ":)":"😊",
    ":(":"😞",
    "*":"🌟",
    "<3":"❤️",
    ":3":"🥴"
}
output=" "
for word in words:
    output+=emojis.get(word,word)+ " "
print(output)
