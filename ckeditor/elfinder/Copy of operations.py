from ckeditor.elfinder.http import HttpRequestParser
from ckeditor.elfinder.builders import ResponseBuilder
from ckeditor.elfinder.commands import OpenCommand

class Operation:
	def __init__(self, request, get=None, post=None):
		print 'building operation ===================================================================================================='
		self.request = HttpRequestParser(request, get=get, post=post)
		print 'building operation 2===================================================================================================='
		self.response = ResponseBuilder()
		print 'building operation 3===================================================================================================='
		self.runable = self.request.fine()
	
	def run(self):
		print 'building response ===================================================================================================='
		#self.response = r'{"cwd":{"mime":"directory","ts":1322613670,"read":1,"write":1,"size":0,"name":"files","hash":"l1_XA","volumeid":"l1_","date":"30 Nov 2011 03:41","locked":1,"dirs":1},"options":{"path":"files","url":"\/elfinder\/php\/..\/files\/","tmbUrl":"\/elfinder\/php\/..\/files\/.tmb\/","disabled":[],"separator":"\\","copyOverwrite":1,"archivers":{"create":[],"extract":[]}},"files":[{"mime":"directory","ts":1322613670,"read":1,"write":1,"size":0,"name":"files","hash":"l1_XA","volumeid":"l1_","date":"30 Nov 2011 03:41","locked":1,"dirs":1},{"mime":"unknown","ts":1322613670,"read":1,"write":1,"size":2,"name":".gitignore","hash":"l1_LmdpdGlnbm9yZQ","phash":"l1_XA","date":"30 Nov 2011 03:41"},{"mime":"directory","ts":1327594870,"read":1,"write":1,"size":0,"name":".tmb","hash":"l1_LnRtYg","phash":"l1_XA","date":"Yesterday 19:21"},{"mime":"application\/zip","ts":1327595028,"read":1,"write":1,"size":103633,"name":"jquery.mobile-1.0b1.zip","hash":"l1_anF1ZXJ5Lm1vYmlsZS0xLjBiMS56aXA","phash":"l1_XA","date":"Yesterday 19:23"},{"mime":"directory","ts":1327594868,"read":1,"write":1,"size":0,"name":"temp","hash":"l1_dGVtcA","phash":"l1_XA","date":"Yesterday 19:21"}],"api":"2.0","uplMaxSize":"2M","debug":{"connector":"php","phpver":"5.3.5","time":1.4434499740601,"memory":"2385Kb \/ 2313Kb \/ 128M","upload":"","volumes":[{"id":"l1_","name":"localfilesystem","mimeDetect":"internal","imgLib":"gd"}],"mountErrors":[]}}'
		if self.runable:
			print 'REQUEST IS FINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEeee2222222222222222222222222222222222222222'
			self.command = self.request.command(request=self.request)
			print 'EXECEUTE COMMMMMMMMAAAAAAAAAANNNNDDDDDS'
			try:
				self.command.execute()
				if self.command.success:
					#self.response.add_command_result(self.command.get_result())
					self.response.add_command_result(self.command)
				else:
					self.response.add_command_error(self.command.get_errors())
			except Exception, e :
				print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!ERRRRR :::: %s' % e
		try:
			self.response.build()
		except Exception, e:
			pass