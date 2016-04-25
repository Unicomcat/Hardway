n = int(raw_input(">"))
try:
	assert n > 2
except:
	raise ValueError("error")
finally:
	print "can you see me?"


