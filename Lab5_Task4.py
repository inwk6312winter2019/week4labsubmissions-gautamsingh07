class Time():

def print_time(self):
	return (self.hours, self.min, self.seconds)

def is_after(t1, t2):
	return (print_time(t1) > print_time(t2))

t1=Time()
t2=Time()
t1.hours=11
t1.min=44
t1.seconds=37
t2.hours=10
t2.min=33
t2.seconds=16

print(is_after(t1,t2))
