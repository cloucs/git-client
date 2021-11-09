# used to create new directory for git repo in the users home directory

import os

class Directory:
	def __init__(self, directory, parent_dir):
		self.directory = directory
		self.parent_dir = parent_dir
		#self.path = os.path.join(self.parent_dir, self.directory)

	def createDir(self):
		#directory = self.directory	
		#self.parent_dir = parent_dir 
		self.path = os.path.join(self.parent_dir, self.directory)
		try:
			os.mkdir(self.path)
			print("directory '%s' created" %self.directory)
		except OSError as error:
			print(error)
		# loggin %self.directoryg
		#print("directory '%s' created" %self.directory)

#testing



		
# TODO: implement solution with file explorer, instead of hardcoding the path
# directory name
#directory = "test-repo"

# parent directory path
#parent_dir = "/home/humanity/"

# mode
#mode = 0o666

# full path
#path = os.path.join(parent_dir, directory)

# create directory
#os.mkdir(path)
# create directory with mode 0o666
#os.mkdir(path, mode)
#print("directory '%s' created" %directory)
