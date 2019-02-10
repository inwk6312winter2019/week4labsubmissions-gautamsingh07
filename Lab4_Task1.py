import string
fin=open('words.txt','r')

for line in fin:
 line = line.strip (string.whitespace + string.punctuation)
 print(line.split())
