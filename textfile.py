F = open("data.txt")
for data in F:
    if data == 'Peter':
        print(data[0:-1])
