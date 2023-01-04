file = open('read')

print(file.read())
file.close()

line = file.readline()
while line !="":
    print(line)
    line=file.readline()

####
for line in file.readlines():
    print(line)

file.close()
