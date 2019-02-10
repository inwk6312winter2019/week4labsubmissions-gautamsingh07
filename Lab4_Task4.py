import string

hist = dict()
list = []

def histogram(filename):
 file = open('filename', "rt")
 for line in file:
  line = line.split()
  for word in line:
   word = word.strip (string.punctuation + string.whitespace).lower()
   hist[word] = hist.get(word, 0)
 return(hist)

def difference(a,b):
    text = set(a)
    word = set(b)
    diff = text.difference(word)

    print("text set:", text)
    print("word set:", word)
    print("words in the book that are not in the word list:")
    print("different set:", diff)
   
file1 = histogram("mybook.txt")
file2 = histogram("words.txt")
difference(file1, file2)
