x = 0
y = 0
total = 0


number = int(input("put in number of names "))
names = [ ]


while number > x:
    acceptedName = str(input("please insert Name"))
    names.append(acceptedName)
    x = x+1

total = len(names)
while total > y:
    print (names.pop(0))
    y = y+1
