import collections

'''Using appendleft and popleft method'''
q = collections.deque()
print(q)
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)
q.popleft()
print(q)

'''Using append and pop method'''
d = collections.deque()
print(d)
d.append(50)
d.append(60)
d.append(70)
print(d)
d.pop()
print(d) 
