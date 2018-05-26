#coding=utf-8
import os

class test(object):
	def __init__(self):
		self.dirp = None

	def testname(self):
		print self.echohello()


	@property	
	def echopath(self):
		return self.dirp

	@echopath.setter
	def echopath(self,value):
		self.dirp = value
		print "hello"

	@classmethod
	def echohello(self):
		return "test%s,%s"%("hello","bod")
		
	def testnocla(self):
		print "theend"

if __name__ == '__main__':
	#testint = test()
	# test.echopath = os.getcwd()
	# print test.echopath
	# test.echohello()
	# testint = test()
	# testint.testnocla()
	t = test()
	t.testname()



# from  testpk import pgf

# t = pgf.P1()

# print t.foo()