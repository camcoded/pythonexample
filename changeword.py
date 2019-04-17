readfile = open("data8.txt","r")
writefile = open("data9.txt","w")

word = ""
for line in readfile:
    i=0
    while i<len(line):
        if charc[i:i+1] == word[i:i+1]:
            if charc[i:i+len(charc)]==word:
                writefile.write(word)
                char[i:i+1]
            else:
                writefile.write(charc)
            
    
writefile.close()
