import sys
from PyQt5.QtWidgets import QApplication
from classes.tformat import TFormat
from classes.app import App
from classes.git import Git

# TODO: remove print() commands

if __name__ == "__main__":
	qApp = QApplication(sys.argv)
	app = App()
	#app.openFileDialog()
	#git = Git(app.createDirectoryDialog())
	#git = Git(app.openDirectoryDialog())
	#git = Git()
	#git.init()
	#git.stageAll()
	#git.commit()
	sys.exit(qApp.exec_())

	# logs end of execution
	t = TFormat()
	print(t.OKGREEN + t.BOLD + "[end of main]" + t.ENDC)
	del t
