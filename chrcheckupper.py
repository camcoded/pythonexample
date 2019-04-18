alpha = ''

message=input("enter any message")

for ch in message:
    ord(ch)>=97:
        if ord(ch)=65 and ord(ch) <=90:
            print(alpha)

    i=0

while i <=25:
    if alpha[i]>0:
        print(chr(i+65),'=',alpha[i])
    i+=1

