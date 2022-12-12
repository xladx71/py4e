fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    #print(words)
    for item in words:
        if item not in lst:
            lst.append(item)
lst.sort()
print(lst)
