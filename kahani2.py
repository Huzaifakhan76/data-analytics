kahani = ""
while True:
    data = input('enter a story=>')
    if len(data) == 0:
        print("the end!")
        break
    kahani += data + "\n"

print("The real story:")
print(kahani)
with open(file.txt, 'w') as file:
    file.write(kahani)
    
