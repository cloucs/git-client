import sys
from PyQt5.QtWidgets import QApplication
from classes.tformat import TFormat
from classes.app import App

if __name__ == "__main__":
	qApp = QApplication(sys.argv)
	app = App()
	#sys.exit(qApp.exec_())

	# logs end of execution
	t = TFormat()
	print(t.OKGREEN + t.BOLD + "[end of main]" + t.ENDC)
	del t
