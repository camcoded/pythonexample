


def findandreplace(find,replace):
    readfile = open("data8.txt","r")
    writefile = open("data9.txt","w")
    
   
    newmessage=" "
    for message in readfile:
        i=0
        while i<len(message): #start of the message
            if message[i:i+1]==find[0:1]: #message from 0:1 is the same as find first letter
                if message[i:i+len(find)]==find:
                    newmessage+=replace
                    i=i+len(find)-1
                else:
                    newmessage+=message[i:i+1]
            else:
                newmessage+=message[i:i+1] #put the first letter in newmessage

            i+=1
    writefile.write(newmessage)

findandreplace("shafeq","****")
