class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __repr__(self):
		return '<Point: {},{}>'.format(self.x, self.y)


p1 = Point(4, 5)
p2 = Point(4, 5)
print(p1 + p2)
