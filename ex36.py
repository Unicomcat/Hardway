import sys 
# this is how with as work

class TestContext(object):
	test_count = 1
	def __init__(self):
		
		print "here is init"
	def __enter__(self):
		#pass
		print "here is enter"
		return self
	def __exit__(self, *args):
		print args
        



with TestContext() as test:
	print 1/0
