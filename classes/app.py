import os
from sys import platform
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QMainWindow, QAction, QMenu
from PyQt5.QtGui import QIcon
from classes.tformat import TFormat
from classes.git import Git

class App(QWidget):
	def __init__(self):
		super().__init__()
		# Log
		self.t = TFormat()
		print(self.t.HEADER + "App.__init__()" + self.t.ENDC)
		self.title = 'Sit - Simple Git'
		self.left = 0
		self.top = 0
		self.width = 340
		self.height = 180
		self.options = QFileDialog.Options()
		self.options |= QFileDialog.DontUseNativeDialog
		self.path = "/home/"
		self.initUI()

	def button_clicked(self):
		print("clicked")

	def layout(self):
		git = Git()

		#hbox
		#open
		self.openBtn = QtWidgets.QPushButton(self)
		self.openBtn.setText("Open")
		self.openBtn.clicked.connect(self.openDirectoryDialog)

		self.hbox = QtWidgets.QHBoxLayout()
		self.hbox.addWidget(self.openBtn)

		#hbox2
		#init
		self.initBtn = QtWidgets.QPushButton(self)
		self.initBtn.setText("Init")
		self.initBtn.clicked.connect(lambda: git.init(self.path))
		
		#stage all
		self.stageAllBtn = QtWidgets.QPushButton(self)
		self.stageAllBtn.setText("Stage All")
		self.stageAllBtn.clicked.connect(lambda: git.stageAll(self.path))
		
		self.hbox2 = QtWidgets.QHBoxLayout()
		self.hbox2.addWidget(self.initBtn)
		self.hbox2.addWidget(self.stageAllBtn)

		#hbox3
		#commit
		self.commitBtn = QtWidgets.QPushButton(self)
		self.commitBtn.setText("Commit")
		self.commitBtn.clicked.connect(lambda: git.commit(self.path))
		
		self.hbox3 = QtWidgets.QHBoxLayout()
		self.hbox3.addWidget(self.commitBtn)

		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addLayout(self.hbox)
		self.vbox.addLayout(self.hbox2)
		self.vbox.addLayout(self.hbox3)

		self.setLayout(self.vbox)

	def initUI(self):
		# Log
		print(self.t.HEADER + "App.initUI()" + self.t.ENDC)
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.layout()
		self.show()

	def openDirectoryDialog(self):
		# Log
		print(self.t.HEADER + "App.openDirectoryDialog()" + self.t.ENDC)
		self.path = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", "", self.options)
		print(self.path)
		return self.path

#TODO: finish this function for git.stageSelected()
#	def openFileDialog(self):
#		# Log
#		print(self.t.HEADER + "App.openFileDialog()" + self.t.ENDC)
#		try:
#			files = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "All Files (*)", "", self.options)
#			print("Files: " + str(files))
#			return files
#		except OSError as error:
#			error = str(error)
#			print(self.t.WARNING + error + self.t.ENDC)
