import os, sys, inspect
from PySide6 import QtCore, QtWidgets, QtUiTools, QtGui

path_to_libs = os.getcwd()
path_to_libs = os.path.join(path_to_libs, "plugins")
sys.path.insert(0, path_to_libs)

class MainWindow(QtWidgets.QMainWindow):
	'''MainWindow class'''
	def __init__(self):
		super().__init__()
	
		self.img_dir = self.open_file()
		self.first, second = os.path.splitext(self.img_dir)

		ui_file = os.getcwd() + "/ui/ui_main_new.ui"
		loader = QtUiTools.QUiLoader()
		ui_file = QtCore.QFile(ui_file)
		ui_file.open(QtCore.QFile.ReadOnly)
		ui = loader.load(ui_file)
		ui_file.close()

		self.setCentralWidget(ui)

		self.vL = ui.findChild(QtWidgets.QVBoxLayout, "verticalLayout_3")

		self.pl()

		self.graphicsview = ui.findChild(QtWidgets.QGraphicsView, "gV")
		self.scene = QtWidgets.QGraphicsScene()
		self.pixmap = QtGui.QPixmap(self.img_dir)
		self.scene.addPixmap(self.pixmap)
		self.graphicsview.setScene(self.scene)
		self.graphicsview.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

	def open_file(self):
		'''Func for choosing an img'''
		file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
		if file_name:
			return file_name
	
	def resizeEvent(self, event):
		'''Обработчик событий на изменение размера окна и соответственно изображения'''
		self.graphicsview.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
		
	def pl(self):
		"""Load && Check plugins"""
		plugin_dir = "plugins"
		modules = []
		buttons = {}

		for fname in os.listdir(plugin_dir):
			if fname.endswith (".py"):
				module_name = fname[: -3]
				print(f"Load module {module_name}")
				# Загружаем модуль и добавляем его имя в список загруженных модулей
				package_obj = __import__(plugin_dir + "." +  module_name)
				modules.append(module_name)
				# print("dir(package_obj) = " + str(dir(package_obj)) + "\n")
			else:
				print("Skip " + fname)

		# Перебираем загруженные модули
		for modulename in modules:
			module_obj = getattr(package_obj, modulename)
			# print(dir(module_obj))
			if not hasattr(module_obj, 'Plugin'):
				print(modulename, 'Модуль не имеет класса Plugin')

		for modulename in modules:
			button = QtWidgets.QPushButton(modulename)
			buttons[modulename] = button
			buttons[modulename].clicked.connect(lambda package=package_obj, mod=modulename: self.handle_plugin_click(package, mod))
			self.vL.addWidget(button)

		return package_obj

	def insert_Image(self, img_dir):
		self.pixmap = QtGui.QPixmap(img_dir)
		self.scene.addPixmap(self.pixmap)
		self.graphicsview.setScene(self.scene)

	def handle_plugin_click(self, package_obj, modulename):
		'''Func(run)'''
		module_obj = getattr(package_obj, modulename)

		for elem in dir(module_obj):
			obj = getattr(module_obj, elem)
			if inspect.isclass(obj):
				a = obj()
				if (a.show_message_box(self.img_dir, self.first)):
					self.insert_Image(self.first + '_main.jpg')

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()