


def findandreplace(find,replace):
    readfile = open("data8.txt","r")
    writefile = open("data9.txt","w")
    
   
    newmessage=" "
    for message in readfile:
        i=0
        while i<len(message): 
            if message[i:i+1]==find[0:1]: 
                if message[i:i+len(find)]==find:
                    newmessage+=replace
                    i=i+len(find)-1
                else:
                    newmessage+=message[i:i+1]
            else:
                newmessage+=message[i:i+1] 

            i+=1
    writefile.write(newmessage)

findandreplace("shafeq","cameron")
