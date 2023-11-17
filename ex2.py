# Implementation of Node class
class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node
	
	def __str__(self):
		to_print = str(self.data) + ' -> '
		temp = self.next
		while temp:
			to_print += str(temp.data) + ' -> '
			temp = temp.next
		to_print += 'None'
		
		return to_print


# 1 - Write a program to reverse a linked list.
def reverse_linked_list(head):
	print("The Linked List Before Reversing: " + str(head))
	last = None
	while head.next is not None:
		temp = head.next
		head.next = last
		last = head
		head = temp
	head.next = last
	print("The Linked List After Reversing: " + str(head))
	print()


# 2 - Write a program to find the middle element of a linked list.
def find_middle_element(head):
	print("The Linked List: " + str(head))
	length = 0
	temp = head
	# find the length od the linked list
	while temp is not None:
		length += 1
		temp = temp.next
	middle_element = None
	middle_index = length // 2 if length % 2 == 0 else length // 2 + 1
	current_index = 0
	# now find the middle element using half of the length
	while head is not None:
		current_index += 1
		if current_index == middle_index:
			middle_element = head
			break
		head = head.next
	
	print("The Middle Element: " + str(middle_element.data))
	print()


# 3 - Write a program to detect if a linked list has a cycle.
class NewNode(Node):
	def __init__(self, data=None, next_node=None, flag=0):
		super().__init__(data, next_node)
		self.flag = flag


def has_cycle(head: NewNode):
	while head is not None:
		if head.flag == 1:
			return True
		head.flag = 1
		head = head.next
	
	return False


if __name__ == '__main__':
	# Question 1
	head_node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	reverse_linked_list(head_node)
	
	# Question 2
	head_middle_node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	find_middle_element(head_middle_node)
	
	# Question 3
	new_head = NewNode(1, NewNode(2, NewNode(3, NewNode(4, NewNode(5)))))
	node = NewNode(6)
	temp = new_head
	# make cycle in linked list
	while temp.next is not None:
		if temp.data == 3:
			node.next = temp
		temp = temp.next
	temp.next = node
	print("Linked List Has Cycle? " + str(has_cycle(new_head)))
