import string

hist = dict()
list = []

def histogram(filename):
 file = open('filename', "rt")
 for line in file:
  line = line.split()
  for word in line:
   word = word.strip (string.punctuation + string.whitespace).lower()
   hist[word] = hist.get(word, 0)+1
 return(hist)
