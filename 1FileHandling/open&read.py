file=open("ex.txt",'r')
type(file)
# print(file)
content1=file.read()
content2=file.readlines()
print(content1)
#print(content2)  #this wil print nothing because pointer in ex.txt read at last point of file
file.seek(0)  #this will bring the pointer at starting point of the file so it will give o/p
print(content2)  #['line1 \n','line2 \n','line3 \n']
content2=[i.rstrip("\n") for i in content2]  # it will remove '\n' from content 2
file.close()

