from threading import *
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.lock_foo = Semaphore()
        self.lock_foo.acquire()
        self.lock_bar = Semaphore()
        self.lock_bar.acquire()
        
    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            
            printFoo()
            self.lock_bar.release()
            self.lock_foo.acquire()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock_bar.acquire()
            printBar()
            
            self.lock_foo.release()
            
            