name = "Exeggutor"
authors = ["Sayantan Chaudhuri <sayantan.chaudhuro@gmail.com>"]
version = 0.0
autoload = True
class_name = "ExeggutorPlugin"
short_description = "Execute ALL the codes!"
long_description = '''A small plug-in to launch/execute/compile/etc codes being edited in Scribes, something it so alarmingly lacks.'''

class ExeggutorPlugin(object):

	def __init__(self, editor):
		self.__editor = editor
		self.__trigger = None

	def load(self):
		from Exeggutor.Trigger import Trigger
		self.__trigger = Trigger(self.__editor)
		return

	def unload(self):
		self.__trigger.destroy()
		return

