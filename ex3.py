from collections import deque
# Normal Queue
# class Queue:
# 	def __init__(self):
# 		self.items = []
# 		self.front = None
# 		self.rear = None
# 		self.__len = 0
#
# 	def enqueue(self, item):
# 		self.items.append(item)
# 		if self.front is None:
# 			self.front = self.items[0]
# 		if self.rear is None:
# 			self.rear = self.items[-1]
# 		self.__len += 1
# 		return True
#
# 	def dequeue(self):
# 		if len(self.items) == 0:
# 			return None
# 		to_return = self.items[0]
# 		if len(self.items) == 1:
# 			self.items = []
# 			self.front = None
# 			self.rear = None
# 		else:
# 			self.items = self.items[1:]
# 			self.front = self.items[0]
# 		self.__len -= 1
# 		return to_return
#
# 	def get_front(self):
# 		return self.front
#
# 	def get_rear(self):
# 		return self.rear
#
# 	def __len__(self):
# 		return self.__len


# Normal Stack
class Stack:
	def __init__(self):
		self.items = []
	
	# add an item to the top of the stack
	def push(self, item):
		self.items.append(item)
	
	# take out the topmost item in the stack and return its value
	def pop(self):
		return self.items.pop() if len(self.items) > 0 else None
	
	# return the value of the topmost item without take it out
	def peek(self):
		return self.items[-1] if len(self.items) > 0 else None
	
	# return the number of items in the stack
	def size(self):
		return len(self.items)
	
	# return if the stack is empty or not
	def empty(self):
		return len(self.items) == 0


# 1 - Implement a stack using two queues.
class StackTwoQueues:
	def __init__(self):
		self.queue1 = deque()
		self.queue2 = deque()
	
	# add an item to the top of the stack
	def push(self, item):
		# push the item just to the first queue
		self.queue1.append(item)
	
	# take out the topmost item in the stack and return its value
	def pop(self):
		# move all the elements from queue1 to queue2 except the last one
		while len(self.queue1) > 1:
			self.queue2.append(self.queue1.popleft())
			
		# dequeue an item if there is
		item = self.queue1.popleft() if len(self.queue1) == 1 else None
		# swap between the two queue
		self.queue1, self.queue2 = self.queue2, self.queue1
		return item
	
	# return the value of the topmost item without take it out
	def peek(self):
		return self.queue1[-1] if len(self.queue1) > 0 else None
	
	# return the number of items in the stack
	def size(self):
		return len(self.queue1)
	
	# return if the stack is empty or not
	def empty(self):
		return len(self.queue1) == 0
	
	
# 2 - Implement a queue using two stacks.
class QueueTwoStacks:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
		self.__len = 0
		
	# add an item to the last of the queue
	def enqueue(self, item):
		self.stack1.push(item)
		self.__len += 1
		
	# take the first item in the queue
	def dequeue(self):
		# check if the two stacks are empty
		if self.stack1.empty() and self.stack2.empty():
			return None
		
		# if the stack2 is empty add all the items from stack 1 to it in reversed order
		if self.stack2.empty():
			while not self.stack1.empty():
				self.stack2.push(self.stack1.pop())
		self.__len -= 1
		return self.stack2.pop()
	
	def __len__(self):
		return self.__len
	
	
# 3 - Write a program to check if a given string of parentheses is balanced.
def check_parenthesis_balanced(expression):
	if len(expression) % 2 == 1:
		return False
	
	# I used the stack and queue that I have implement above to check their functionality, and it seems to work good
	stack = StackTwoQueues()
	queue = QueueTwoStacks()
	# mapping for each opening parenthesis to its closing one
	parenthesis_dict = {'(': ')', '[': ']', '{': '}'}
	# add all the characters of the expression to the stack and queue
	for x in expression:
		stack.push(x)
		queue.enqueue(x)
	
	"""
	take one time the front item and another from the back and then compare them if they are equal
	then the expression is balanced
	"""
	for _ in range(len(queue) // 2):
		left = queue.dequeue()
		right = stack.pop()
		try:
			if parenthesis_dict[left] != right:
				return False
		except KeyError:
			return False
	
	return True


if __name__ == '__main__':
	print(check_parenthesis_balanced('()'))
	print(check_parenthesis_balanced('{}'))
	print(check_parenthesis_balanced('[]'))
	print(check_parenthesis_balanced('({[]})'))
	print(check_parenthesis_balanced('((()))'))
	print(check_parenthesis_balanced('{[()]}'))
	print(check_parenthesis_balanced('('))
	print(check_parenthesis_balanced(')('))
	print(check_parenthesis_balanced('({[})'))
	print(check_parenthesis_balanced('((())'))
	print(check_parenthesis_balanced('(()))'))
	print(check_parenthesis_balanced('{[(])}'))
	
	"""
	assert check_parenthesis_balanced('()') is True
	assert check_parenthesis_balanced('{}') is True
	assert check_parenthesis_balanced('[]') is True
	assert check_parenthesis_balanced('({[]})') is True
	assert check_parenthesis_balanced('((()))') is True
	assert check_parenthesis_balanced('{[()]}') is True
	assert check_parenthesis_balanced('(') is False
	assert check_parenthesis_balanced(')(') is False
	assert check_parenthesis_balanced('({[})') is False
	assert check_parenthesis_balanced('((())') is False
	assert check_parenthesis_balanced('(()))') is False
	assert check_parenthesis_balanced('{[(])}') is False
	"""

