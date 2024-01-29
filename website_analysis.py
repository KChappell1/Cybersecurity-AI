website = input("Enter a website url: ")

pun = 0 

for i in website:
    punctuation = "`~!@#$%^&*()_-+=}{]{|:;<,>.?/"
    if i in punctuation: 
        pun += 1
print(pun)