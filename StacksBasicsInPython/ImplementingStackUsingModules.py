import collections
import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.get())
print(stack.get())
print(stack.get())
'''It will wait for the 2 seconds after that, it'll give Queue is Empty" message'''
print(stack.get(timeout=2))
