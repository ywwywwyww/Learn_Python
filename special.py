class student:
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return 'student : name = %s' % self.name
		
	__repr__ = __str__
	
	def  __getattr__(self, attr):
		if attr == 'score':
			return 'zjtioi2019ak'
			
	def __call__(self):
		print("zjt ioi ak")

a = student('zjtioiak')

print(a)

print(a.score)

a()

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
		
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a+b
		return a
		
'''	
for n in fib():
	print(n)
	
	
for n in fib():
	print(type(n))
	print(isinstance(n, int))
	print(isinstance(n, fib))
'''

'''
f = fib()

for n in range(10):
	print(f[n])
'''


