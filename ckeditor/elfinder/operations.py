from ckeditor.elfinder.http import HttpRequestParser
from ckeditor.elfinder.builders import ResponseBuilder

class Operation:
	def __init__(self, request, get=None, post=None, files=None):
		self.request = HttpRequestParser(request, get=get, post=post, files=files)
		self.response = ResponseBuilder()
		self.runable = self.request.ok()
	def run(self):
		if self.runable:
			self.command = self.request.command(request=self.request)
			try:
				self.command.run()
				if self.command.success:
					self.response.add_command_result(self.command)
				else:
					self.response.add_command_error(self.command.get_errors())
			except Exception, e :
				print e
		try:
			self.response.build()
		except Exception, e:
			pass
