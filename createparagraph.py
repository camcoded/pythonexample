
def wordcourt(message):
    word = ""

    for x in message:
        if x == " ":
            print(word)
            word=""
        else:
            word+=x
    print(word)
     

wordcourt("hello my friends")
        


