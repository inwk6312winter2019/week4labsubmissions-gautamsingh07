import string

count = 0
d1 =dict()
d2 =dict()
file1 = open("58820-0.txt")
for line in file1:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
       print(word.strip(string.punctuation))
       count = count +1
       if word not in d:
         d[word] = 1
       else:
         d[word] += 1

print(count)
