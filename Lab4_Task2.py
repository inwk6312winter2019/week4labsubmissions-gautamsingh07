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
         d1[word] = 1
       else:
         d1[word] += 1

print(count)


file2 = open("58809-0.txt")
for line in file2:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
       print(word.strip(string.punctuation))
       count = count +1
       if word not in d1:
          d2[word] = 1
       else:
          d2[word] += 1
print(count)

print(len(d))
print(len(d1))

