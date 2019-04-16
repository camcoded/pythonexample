readfile = open("data5.txt","r")

writefile = open("data6.txt","w")

for x in readfile:
    writefile.write(x)
writefile.close()

