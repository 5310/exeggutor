from SCRIBES.SignalConnectionManager import SignalManager
import os

class Exeggutor(SignalManager):

	def __init__(self, manager, editor):
		SignalManager.__init__(self)
		self.__init_attributes(manager, editor)
		self.connect(manager, "activate", self.__activate_cb)
		self.connect(manager, "destroy", self.__destroy_cb)

	def __init_attributes(self, manager, editor):
		self.__manager = manager
		self.__editor = editor
		return
	
	def __exeggutor(self):
		message = "Exeggute ALL the things!"
		uri = str(self.__editor.uri)
		term = "gnome-terminal -x sh -c "
		# Update the message bar.
		self.__editor.update_message(message, "yes", 10)
		# DO THE REAL THING!
		os.system(term+'\"'+'python "'+uri[7:]+'" & '+"python -c 'raw_input()'"+'\"')
		return False

	def __activate_cb(self, *args):
		self.__exeggutor()
		return False

	def __destroy_cb(self, *args):
		self.disconnect()
		del self
		return False

