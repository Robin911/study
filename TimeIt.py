import datetime
import time
from functools import wraps


class TimeIt:
	def __init__(self, fn):
		print('init')
		self._fn = fn
		# functools中的wraps装饰器函数
		wraps(fn)(self)

	def __enter__(self):
		print('enter')
		self.start = datetime.datetime.now()
		return self

	def __call__(self, *args, **kwargs):
		print('__call__')
		start = datetime.datetime.now()
		ret = self._fn(*args, **kwargs)
		delta = (datetime.datetime.now() - start).total_seconds()
		print("dec {} took {}".format(self._fn.__name__, delta))
		return ret

	def __exit__(self, exc_type, exc_val, exc_tb):
		print('exit')
		delta = (datetime.datetime.now() - self.start).total_seconds()
		print("context {} took {}".format(self._fn.__name__, delta))
		return


# 1. 第一种方法，定义函数，通过上下文的方式执行,
def add(x, y):
	time.sleep(2)
	return x + y


with TimeIt(add) as foo:  # enter, 进入时执行；exit, 退出时执行
	print(foo(5, 6))


# 2. 第二种方式，通过类装饰器方式计算运行时间
@TimeIt
def add(x, y):  # add = TimeIt(add)
	"""This is a add function."""
	time.sleep(2)
	return x + y


print(add(10, 11))

print(add.__doc__)
print(add.__name__)
print(add.__dict__)
