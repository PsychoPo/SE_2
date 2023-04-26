# from abc import ABCMeta, abstractmethod, abstractproperty
class InterfacePlugin(object):
	def run(self):
		pass
	
	# """Interface plugin"""
	# # __metaclass__ = ABCMeta

	# # @abstractproperty
	# def PluginName():
	#     """Имя плагина"""

	# @abstractproperty
	# def PluginDescription():
	#     """Описание плагина"""

	# @abstractproperty
	# def Author():
	#     """Автор плагина"""

	# @abstractproperty
	# def Version():
	#     """Версия плагина"""

	# @abstractmethod
	# def ShowInfo(self):
	#     """Показать информацию"""

	# @abstractmethod
	# def run(self):
	#     """Наложение фильтра"""