import os

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from classes.tformat import TFormat

class App(QWidget):
	def __init__(self):
		super().__init__()
		# Log
		self.t = TFormat()
		print(self.t.HEADER + "App.__init__()" + self.t.ENDC)
		self.title = 'Sit - Simple Git'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.options = QFileDialog.Options()
		self.options |= QFileDialog.DontUseNativeDialog
		self.initUI()

	def initUI(self):
		# Log
		print(self.t.HEADER + "App.initUI()" + self.t.ENDC)
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		#self.openDirectoryDialog() 
		#self.createDirectoryDialog()
		self.show()

	def openDirectoryDialog(self):
		# Log
		print(self.t.HEADER + "App.openDirectoryDialog()" + self.t.ENDC)
		#options = QFileDialog.Options()
		#options |= QFileDialog.DontUseNativeDialog
		#dirName = QFileDialog.getExistingDirectory(self,"QFileFialog.getExistingDirectory()","",options=options)
		#dirName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()","",self.options)
		self.path = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()","",self.options)
		return self.path

	def createDirectoryDialog(self):
		# Log
		print(self.t.HEADER + "App.createDirectoryDialog()" + self.t.ENDC)
		# TODO: input through PyQt instead of terminal
		print("Enter directory name: ")
		self.directory = input()
		self.path = os.path.join(self.openDirectoryDialog(), self.directory)
		try:
			os.mkdir(self.path)
			print(self.t.OKGREEN + "Directory '{}' created!".format(self.path) + self.t.ENDC)
			return self.path
		except OSError as error:
			# TODO: PyQt popup instead of terminal output
			error = str(error)
			print(self.t.WARNING + error + self.t.ENDC)
