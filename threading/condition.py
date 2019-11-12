from threading import Condition, Event, Thread
import logging
import random

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class Dispatcher:
	def __init__(self):
		self.data = None
		self.event = Event()
		self.cond = Condition()

	def produce(self, total):
		for _ in range(total):
			self.data = random.randint(0, 100)
			with self.cond:
				logging.info(self.data)
				self.cond.notify_all()
				# self.cond.notify(n=2)
			self.event.wait(1)
		self.event.set()

	def consume(self):
		while not self.event.is_set():
			with self.cond:
				self.cond.wait()
				logging.info("recieved {}".format(self.data))


d = Dispatcher()
p = Thread(target=d.produce, args=(5,), name='produce')
for i in range(5):
	Thread(target=d.consume, name='consume-{}'.format(i)).start()
p.start()
