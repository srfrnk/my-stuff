import sublime, sublime_plugin

class LogCommandsCommand(sublime_plugin.ApplicationCommand):
	state=False
	def run(self,enable,toggle):
		if toggle:
			self.state=not self.state
		else:
			self.state=enable
		sublime.log_commands(self.state)

