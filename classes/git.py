import os
from classes.tformat import TFormat

class Git():
	def __init__(self):
		# Log
		self.t = TFormat()
		print(self.t.HEADER + "Git.__init__()" + self.t.ENDC)

	def init(self, path):
		# Log
		print(self.t.HEADER + "Git.init()" + self.t.ENDC)
		print(self.t.HEADER + "from Git.init(): git init {}".format(path) + self.t.ENDC)
		try:
			os.popen("git init {}".format(path))
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC)
		
	def stageAll(self, path):
		# Log
		print(self.t.HEADER + "Git.stageAll()" + self.t.ENDC)
		print(self.t.HEADER + "from Git.stageAll(): git -C {} add .".format(path) + self.t.ENDC)
		try:
			os.popen("git -C {} add .".format(path))
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC)

#	def stageSelected(self):
#		# Log
#		print(self.t.HEADER + "Git.stageSelected()" + self.t.ENDC)
#		print(self.t.HEADER + "from Git.stageSelected(): git add {}".format("""# TODO: insert list of files a+ path""") + self.t.ENDC)
#		try:
#			os.popen("git add {}".format("""# TODO: insert list of files"""))
#		except OSError as error:
#			error = str(error)
#			print(self.t.WARNING + error + self.t.ENDC)

	def commit(self, path):
		# Log
		print(self.t.HEADER + "Git.commit()" + self.t.ENDC)
		try:	
			os.popen("cd {} && git commit -m 'This is a commit.'".format(path))	
			print("commited")
		except OSError as error:
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC) 
