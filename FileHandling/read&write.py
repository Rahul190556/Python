file=open("ex1.txt",'w')
file.write("Line 1\n")
file.write("Line 2")
file.close() # your will change in your file if you will close it 

file=open("ex1.txt",'w')
l=["Line4","Line5","Line6"]
for item in l:
  file.write(item+"\n")
file.close()  # after writing again previous data will removed