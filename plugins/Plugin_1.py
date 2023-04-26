import Interface

class Plugin_1(Interface.InterfacePlugin):
	# def __init__():
	# self.PluginName = "GrayScaleImage"
	# self.PluginDescription = "Плагин позволяет применить черно-белый фильтр на изображение"
	# self.Author = "Roman Sukhachev"
	# self.Version = 1

	# def ShowInfo(self):
	# """НАЖАТИЕ НА ТУЛ СТРИПЕ"""
	# print(f"showed info BY {self.PluginName}")

	def run(self):
		print("RAN BY Plugin1")