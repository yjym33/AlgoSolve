https://www.acmicpc.net/problem/18258

from collections import deque
import sys
 
 
class Queue:
    """ implementation Queue
        -> push X : push x element
        -> front : pop top element if it is empty return -1
        -> back : pop back element if it is empty return -1
        -> size : return size of stack
        -> empty : check empty if it is return 1 or 0
        -> top : print top element
    """
    memory = deque()
    answer = deque()
    def push(self , X):
        self.memory.append(X)
    
    def pop(self):
        if len(self.memory) == 0:
            self.answer.append(-1)
        else:
            self.answer.append(self.memory[0])
            self.memory.popleft()
    def size(self):
        self.answer.append(len(self.memory))
    
    def empty(self):
        if len(self.memory) != 0:
            self.answer.append(0)
        else:
            self.answer.append(1)
    
    def front(self):
        if len(self.memory) != 0:
            self.answer.append(self.memory[0])
        else:
            self.answer.append(-1)
    
    def back(self):
        if len(self.memory) != 0:
            self.answer.append(self.memory[len(self.memory)-1])
        else:
            self.answer.append(-1)
 
n = int(input())
queue = Queue()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'front':
        queue.front()
    elif cmd[0] == 'back':
        queue.back()
    elif cmd[0] == 'size':
        queue.size()
    elif cmd[0] == 'empty':
        queue.empty()
    elif cmd[0] == 'pop':
        queue.pop()
 
print(*queue.answer)
