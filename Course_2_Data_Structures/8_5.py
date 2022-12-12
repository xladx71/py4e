fname = input("Enter file name: ")
count = 0
fh = open(fname)
for line in fh:
    if len(fname) < 1:
        print('No Text Found')
        quit()
    if line.startswith('From:'):
            continue
    if line.startswith('From'):
        words = line.split()
        print(words[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
