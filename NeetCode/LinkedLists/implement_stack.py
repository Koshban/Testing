'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
Example 1:

Input: ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 2, 2, false]
Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

'''
import queue
from collections import deque

class MyStack:

    def __init__(self):
        self.mystack = deque()
        self.queue = queue.Queue()
        
        

    def push(self, x: int) -> None:
        self.queue.put(x)
        # or
        self.mystack.append(x)
        

    def pop(self) -> int:       
    
        for i in range(len(self.mystack) -1): # do not pop the last item
            self.push(self.mystack.popleft())
        
        return self.mystack.popleft()
        
        # or
        return self.mystack.pop()
        

    def top(self) -> int:
        return self.mystack[-1]
        

    def empty(self) -> bool:
        return len(self.mystack) == 0
    # or return self.queue.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()