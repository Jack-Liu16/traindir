#coding=utf-8

class P1(object): 
   def foo(self):           
       print('p1-foo') 
class P2(object): 
   def foo(self): 
       print('p2-foo')
   def bar(self): 
       print('p2-bar') 
class C1 (P1,P2):
   def bar(self):
      super(C1,self).bar()

      #pass  
class C2 (P1,P2): 
   def bar(self): 
       print('C2-bar')  
class D(C1,C2): 
   pass


def test():
  print "this__name__ is:%s"%__name__

if __name__ == 'testpk.pgf':
  print "testok 已经执行到模块(%s):  if __name__ == 'testpk.pgf'的代码了"%__name__
  #print dir()
#c = C1()
#c.bar()
# d=D() 
# d.foo() # 输出 p1-foo 
# d.bar() # 输出 p2-bar 