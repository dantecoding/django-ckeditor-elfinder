import UserDict
from django.utils import simplejson as json

class ResponseBuilder(UserDict.IterableUserDict, object):
	def __init__(self, *args, **kwargs):
		super(ResponseBuilder, self).__init__()
		self.mimetype = 'application/json'
		self.json_result = ''
		self.other_result = ''
		self.headers = None
	def build(self):
		if self.mimetype == 'application/json':
			self.json_result = json.dumps(dict(self))
		
	def add_command_result(self, command):
		result = command.get_result()
		self.mimetype = command.get_result_type()
		self.headers = command.get_headers()
		if type(result) in (type([]), type(())):
			for r in result:
				self.update(r)
		elif type(result) == type({}):
			self.update(result)
		else:
			self.other_result = result
			self.json_result = result
	def add_command_error(self, error):
		self.update({'error': error})
		
	def get_result(self):
		if self.other_result:
			return self.other_result
		return self.json_result