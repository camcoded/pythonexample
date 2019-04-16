FR = open("file.txt","r")
FW = open("file2.txt","w")

for Line in FR:
    for character in Line:
        if character == "o":
            FW.write("*")
        else:
            FW.write(character)
FW.close()
