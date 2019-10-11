class Item:
	def __init__(self, name, **kwargs):
		self.name = name
		self.spec = kwargs

	def __repr__(self):
		return "{} = {}".format(self.name, self.spec.keys())


class Cart:
	def __init__(self):
		self.item = []

	def __len__(self):
		return len(self.item)

	def additem(self, item):
		self.item.append(item)

	def __add__(self, other):
		if isinstance(other, int):
			self.item.append(other)
			return self
		else:
			print("{},不是Item类型！".format(other))

	def __getitem__(self, index):
		return self.item[index]

	def __setitem__(self, key, value):
		self.item[key] = value

	def __iter__(self):
		return iter(self.item)

	# def __missing__(self, key)  # 只支持字典key不存在的时候触发
	# 	print(key)

	def __repr__(self):
		return str(self.item)


cart = Cart()
print(cart + 2 + 3 + 4 + 5)
print(len(cart))
for x in cart:
	print(x)
