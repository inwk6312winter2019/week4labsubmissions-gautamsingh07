import string

def remove(word):
 pun = string.punctuation
 str = ""
 for p in pun:
  str = word.strip() 
  str = word.replace(p,'')
 return str
