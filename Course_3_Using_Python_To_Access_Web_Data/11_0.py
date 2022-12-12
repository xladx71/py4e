import re
#fname = input('Enter file name:')
hand = open('regex_sum_1419206.txt')
numlist_strings = []
numlist = []

for line in hand:
    line = line.strip()
    s = re.findall('[0-9]+', line)
    if len(s) > 0:
        for x in s:
            numlist_strings.append(x)
for y in numlist_strings:
        numlist.append(int(y))
        #print('+',y)
        #print(sum(numlist))
print(sum(numlist))


# for fun

#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
