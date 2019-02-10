import string

def remove(word):
 pun = string.punctuation
 str = ""
 for p in pun:
  str = word.strip() 
  str = word.replace(p,'')
 return str


def sed(file1,file2):
 try:
  f1 = open(filename1,"r")
  f2 = open(filename2,"w")
   for char in f1 :
    new = removepattern(char)
    f2.write(cgar)
   print("File Modified")
 except:
  print("Operation Failed")


