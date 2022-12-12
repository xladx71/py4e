name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
cntr = {}
for line in handle:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words = line.split()
        clock  = (words[5])
        time = clock.split(':')
        hour = time[0]
        lst.append(hour)
for c in lst :
    cntr[c] = cntr.get(c, 0) + 1
t = list(cntr.items())
t.sort()
for key, val in t:
    print(key,val)
