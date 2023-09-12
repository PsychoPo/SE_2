from os.path import splitext, basename
from sys import argv
from PIL import Image
from PySide6.QtWidgets import QMessageBox

class Plugin:
	PluginName = "GrayScaleImage"
	PluginDescription = "Плагин позволяет применить черно-белый фильтр на изображение."
	Author = "Roman Sukhachev."
	Version = 1

	def show_message_box(self, img_dir, first):
		'''Вызов QMessageBox'''
		msg_box = QMessageBox(QMessageBox.Information, "PluginInfo", f"{self.PluginName} - {self.PluginDescription}\nАвтор: {self.Author}\nВерсия: {self.Version}", QMessageBox.Ok | QMessageBox.Cancel)
		if msg_box.exec() == QMessageBox.Ok:
			self.run(img_dir, first)
			return True
		else:
			return False

	def run(self, img_dir, first):
		image = Image.open(img_dir)

		image = image.convert('L')

		image.save(first + '_' + splitext(basename(argv[0]))[0] + '.jpg')
		
		print(f"{self.PluginName} done!")