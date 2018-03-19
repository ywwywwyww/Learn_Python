class student:
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return 'student : name = %s' % self.name
		
	__repr__ = __str__

print(student('zjt ioi ak'))

class fib:
	def __init__(self):
		self.a, self.b = 0, 1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if(self.a > 10000):
			raise StopIteration()
		return self.a
	
for n in fib():
	print(n)
	
	
for n in fib():
	print(type(n))
	print(isinstance(n, int))
	print(isinstance(n, fib))
