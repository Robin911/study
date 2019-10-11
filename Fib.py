class Fib:
	def __init__(self):
		self.lst = [0, 1, 1]

	def __iter__(self):
		return iter(self.lst)

	def __len__(self):
		return len(self.lst)

	def __call__(self, x):
		if x < len(self.lst):
			return self.lst
		for i in range(len(self.lst) - 1, x):
			self.lst.append(self.lst[i - 1] + self.lst[i])
		return self.lst

	def __getitem__(self, index):
		if index < 0:
			return None
		if index < len(self):
			return self.lst[index]
		self(index)


a = Fib()
print(a(5))

print(a(5))
print(a[8])
print(a[7])
