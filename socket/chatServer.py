#-*- coding : utf-8 -*-
# coding: utf-8
import socket
import logging
import threading
import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(thread)d %(message)s")


class ChatServer:
	def __init__(self, ip='127.0.0.1', port=9999):
		self.sock = socket.socket()
		self.addr = (ip, port)
		self.clients = {}

	def start(self):
		self.sock.bind(self.addr)
		self.sock.listen()
		threading.Thread(target=self._accept).start()

	def _accept(self):
		while True:
			conn, client = self.sock.accept()
			self.clients[client] = conn
			print(self.clients[client])
			threading.Thread(target=self._recv, args=(conn, client), name='recv').start()

	def _recv(self, conn, client):
		while True:
			data = conn.recv(1024)
			msg = "{}:{}\t{}".format(*client, data)
			#print(data.decode(''))
			logging.info(msg)
			msg = msg.encode()
			for s in self.clients.values():
				s.send(msg)

	def stop(self):
		for s in self.clients.values():
			s.close()
		self.sock.close()


cs = ChatServer()
cs.start()
