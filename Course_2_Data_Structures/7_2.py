# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
total = 0
seq = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence"):
        #tolly = line.find('0')
        tolly = line[20:]
        total = total + float(tolly)
        seq = seq + 1
        #print(total)
print('Average spam confidence:',total / seq)
