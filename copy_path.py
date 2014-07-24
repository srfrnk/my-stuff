import sublime, sublime_plugin

class CopyPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	sublime.set_clipboard(self.view.file_name());