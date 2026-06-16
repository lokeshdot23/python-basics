#Queue Data structures - FIFO
'''
Tail - insertion
Head - deletion
               ----------
Head(insertion)|10|20|30| Tail(Deletion)
               ----------

Overflow, Underflow(works in queue), isempty(works in stack)
enqueue - append
dequeue - pop(i)
peak[0]

Import queue
1. Add item -> append(x) -> put(x)
2. Remove item -> popleft(x)/pop(i) -> get(x)
3. size -> q.qsize()
4. empty -> q.empty()
'''
'''
#Implementation of stack using queue
from queue import Queue
class stack:
    def __init__(self):
        self.q = Queue()
    def push(self,x):
        size = self.q.qsize()
        self.q.put(x)
        for i in range(size):
            self.q.put(self.q.get())
    def pop(self):
        if self.q.empty():
            print("Stack empty")
        else:
            print("Popped:",self.q.get())
    def top(self):
        if self.q.empty():
            print("Stack empty")
        else:
            print("Top:",self.q.queue[0])
    def display(self):
        print("Stack:",list(self.q.queue))
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.top()
s.pop()
s.display()
'''
from queue import Queue
q1=Queue()
q2=Queue()
q1.put(10)
q1.put(11)
q1.put(12)
while q1.qsize()>1:
    q2.put(q1.get())
print("popped",q1.get())
while not q2.empty():
    q1.put(q2.get())
print("remaining stack",list(q1.queue))
