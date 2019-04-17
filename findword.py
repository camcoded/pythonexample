def look(message,find,replace):
    i=0
    found=0
    x=0
    while i<len(message):
        if message[i:i+1]==find[0:1]:
                            if message[i:i+len(find)]==find:
                                if message[x:x+len(find)]==replace:
                                    


                                found+=1
                                i=i+len(find)-1




                               
        i+=1

        
            
            
       
    print("we found",found,find)
look("hi my name is peter, hi peter","peter","shafeq)
