import os
from classes.tformat import TFormat
from classes.app import App

class Git():
	def __init__(self, path):
		# Log
		self.t = TFormat()
		print(self.t.HEADER + "Git.__init__()" + self.t.ENDC)
		self.path = path

	def init(self):
		# Log
		print(self.t.HEADER + "Git.init()" + self.t.ENDC)
		print(self.t.HEADER + "from Git.init(): git init '{}'".format(self.path) + self.t.ENDC)
		try:
			os.popen("git init '{}'".format(self.path))
			#self.stream = os.popen("git init")
			#output = stream.read()
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC)
		
	def stageAll(self):
		# TODO: fix error
		# Log
		print(self.t.HEADER + "Git.stageAll()" + self.t.ENDC)
		print(self.t.HEADER + "from Git.stageAll(): git add '{}'".format(self.path) + self.t.ENDC)
		try:
			os.popen("git add '{}'".format(self.path))
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC)

	def commit(self):
		# Log
		print(self.t.HEADER + "Git.commit()" + self.t.ENDC)
		print("Enter commit message: ")
		self.commitMsg = input()
		try:	
			os.popen("git commit -m '{}'".format(self.commitMsg))
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC) 
