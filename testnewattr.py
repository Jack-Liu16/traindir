# #coding=utf-8
# from  testpk import newattr


# obj1 = newattr.Singleton()

# obj1.attr1 = "test1"

# print obj1.attr1


def fornum(maxram):
	fornum = 1
	renum = 2
	for i in range(1,maxram):
		renum *=2
		fornum +=1
		if renum >= maxram:
			return fornum
val = []
for i in range(1,10):
	val.append(i)

print val	
#print fornum(16)