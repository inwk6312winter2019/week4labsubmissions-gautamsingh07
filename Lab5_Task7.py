class kangaroo():
	
 def __init__(self, pouch= []):
  self.pouch = pouch

 def put_in_pouch(self, other):
  self.pouch = other

 def __str__(self):
  return (self, self.pouch)
