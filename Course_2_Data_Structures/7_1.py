# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
turnip = fh.read()

tei = turnip.strip()

print(tei.upper())
