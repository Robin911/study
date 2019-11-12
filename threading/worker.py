from threading import Event, Thread
import logging
import time

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def boss(event: Event):
	logging.info("bossssssssssssssssssssssssssss")
	event.wait()
	logging.info("okkkkkkkkkkkkkkkkkkkkkkkkkkkk")


def worker(event: Event, count=10):
	logging.info("workinggggggggggggggggggg")
	cups = []
	while True:
		logging.info('make 1111111111')
		time.sleep(0.5)
		cups.append(1)
		if len(cups) >= count:
			event.set()
			break
	logging.info('I finished my job. cups={}'.format(cups))


event = Event()
w = Thread(target=worker, args=(event,))
b = Thread(target=boss, args=(event,))
w.start()
b.start()