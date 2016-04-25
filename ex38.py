# the method must have self
class Thing(object):
	def test(self,hi):
		print "hi"
	@staticmethod
	def test1(hi):
		print "hi2"
	@classmethod
	def test2(self,hi):
		print "hi3"
a = Thing()

a.test("hello")
a.test1("haha")
Thing.test1("haha")
Thing.test2("haha")
a.test2("haha")


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)

print " There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print "#".join(stuff[3:5])
print (3,4)
