from classes.directory import Directory
from classes.tformat import TFormat
if __name__ == "__main__":
	# class instantiation
	t = TFormat()
	dir = Directory("test-repo", "/home/humanity/")
	# create new directory
	dir.createDir()
	del dir
	
	# logs end of execution
	print(t.OKGREEN + t.BOLD + "[end of main]" + t.ENDC)
