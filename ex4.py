# Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1 - Write a program to find the lowest common ancestor of two nodes in a binary tree.
def find_lowest_common_ancestor(root, node1, node2):
    # if one of the nodes is the root of the binary tree so the lowest common ancestor is the root
    if root is None or root.value == node1.value or root.value == node2.value:
        return root
    
    # now we search in left and right subtrees
    left_ancestor = find_lowest_common_ancestor(root.left, node1, node2)
    right_ancestor = find_lowest_common_ancestor(root.right, node1, node2)
    
    # if we find the lowest ancestor in each subtree this means that the root is the lowest ancestor
    if left_ancestor and right_ancestor:
        return root
    
    # if one of them not None so it is the lowest common ancestor and return it
    if left_ancestor:
        return left_ancestor
    return right_ancestor


# 2 - Write a program to find the shortest path between two nodes in a graph.
# want to make new node class to use in the BFS search below
class BFSNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = dict()
        
        
def find_shortest_path_between_two_nodes(source, destination):
    from collections import deque
    
    if source is None or destination is None:
        return None
    
    if source == destination:
        return destination
    
    visited_nodes = set()
    queue = deque()
    queue.append([(source, [source])])
    while len(queue) > 0:
        node, path = queue.popleft()
        if node.value == destination.value:
            return path
        
        if node not in visited_nodes:
            visited_nodes.add(node)
            for neighbor in node.neighbors.values():
                if neighbor not in visited_nodes:
                    queue.append((neighbor, path + [neighbor]))
                    
    return None
    

# 3 - Implement a binary search tree and write functions to insert, delete and search for elements.
# Binary Search Tree
class BinarySearchTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def insert(self, value):
        self._insert_helper(self.root, value)
        
    def _insert_helper(self, root, value):
        if root is None:
            return
        if value < root.value:
            if not root.left:
                root.left = Node(value)
                return
            else:
                self._insert_helper(root.left, value)
        elif value > root.value:
            if not root.right:
                root.right = Node(value)
                return
            else:
                self._insert_helper(root.right, value)
    
    def delete(self, value):
        self.root = self._delete_helper(self.root, value)
            
    def _delete_helper(self, root, value):
        if root is None:
            return root
            
        # Search for the node to be deleted
        if value < root.value:
            root.left = self._delete_helper(root.left, value)
        elif value > root.value:
            root.right = self._delete_helper(root.right, value)
        else:
            # if the root node is the wanted node
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # if the wanted node has two children
            # Find the largest node after the root in value, that will be smallest in the right subtree
            current = root.right
            while current.left is not None:
                current = current.left
            root.value = current.value
            # After we take the new node, we want delete its past appearance
            root.right = self._delete_helper(root.right, root.value)
        
        return root
    
    def search(self, value):
        return self._search_helper(self.root, value)
    
    def _search_helper(self, root, value):
        if root is None:
            return None
        
        if value < root.value:
            return self._search_helper(root.left, value)
        elif value > root.value:
            return self._search_helper(root.right, value)
        
        return root
    
    def inorder_traversal(self, root):
        if root:
            # Traverse the left subtree
            self.inorder_traversal(root.left)
            # Print the current node's key
            print(root.value, end=" ")
            # Traverse the right subtree
            self.inorder_traversal(root.right)


if __name__ == '__main__':
    # Question 1
    tree_anc = BinarySearchTree(3)
    tree_anc.left = Node(5)
    tree_anc.right = Node(1)
    tree_anc.left.left = Node(6)
    tree_anc.left.right = Node(2)
    tree_anc.right.left = Node(0)
    tree_anc.right.right = Node(8)
    tree_anc.left.right.left = Node(7)
    tree_anc.left.right.right = Node(4)
    
    node1 = Node(5)
    node2 = Node(1)
    
    print("Lowest Common Ancestor: " + find_lowest_common_ancestor(tree_anc.root, node1, node2))
    
    # Question 2
    # building the graph
    node1 = BFSNode(1)
    node2 = BFSNode(2)
    node3 = BFSNode(3)
    node4 = BFSNode(4)
    node5 = BFSNode(5)
    node6 = BFSNode(6)
    
    # making neighborhood
    def add_edge(node1, node2):
        node1.neighbors[node2.value] = node2
        node2.neighbors[node1.value] = node1
    
    add_edge(node1, node2)
    add_edge(node1, node3)
    add_edge(node2, node4)
    add_edge(node2, node5)
    add_edge(node3, node6)
    
    print(f"Shortest Path Between {node1.value} & {node6.value}: " + find_shortest_path_between_two_nodes(node1, node6))
    
    # Question 3
    tree = BinarySearchTree(5)
    tree.root.left = Node(3)
    tree.root.right = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(6)
    tree.insert(8)
    # tree.root.right.right = Node(8)
    tree.inorder_traversal(tree.root)
