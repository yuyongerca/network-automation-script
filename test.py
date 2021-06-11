

try:
    with open("test.txt", "a") as file:
        file.write("i love the world ")

except IOError as e:
    print ("Unable to open file") #Does not exist OR no read permissions