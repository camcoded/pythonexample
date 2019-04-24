import pdb
pdb.set_trace()
F = open("data.txt")
for data in F:
    if data == 'Peter':
        print(data[0:-1])
