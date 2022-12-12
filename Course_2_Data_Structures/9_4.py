name = input("Enter file:")
if len(name) < 1:
  name = "mbox-short.txt"
handle = open(name)

cntr = {}
lst = []
for line in handle :
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        #print(words)
        lst.append(words[1])
for c in lst :
    cntr[c] = cntr.get(c, 0) + 1
bigmost = None
bigval  = None
for key,val in cntr.items():
    #print(key,val)
    if bigval is None or val > bigval:
        bigmost = key
        bigval = val
print(bigmost, bigval)
