with open("ex3.txt",'a+') as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 15")

print(content) # it will print content in file before adding Line 15 but there is changes in original file