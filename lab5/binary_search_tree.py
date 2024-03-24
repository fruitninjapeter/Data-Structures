class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None

    def __eq__(self, other):
        return isinstance(other, type(self))\
            and self.data == other.data\
            and self.left == other.left\
            and self.right == other.right

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = TreeNode(root)
        self.num_nodes = 0

    def insert(self, newkey):  # inserts a node with key into the correct position if not a duplicate.
        if self.root.key is None:   # if no root node, new node is root node
            self.root.key = newkey
            self.num_nodes += 1
        else:
            self.insert_help(self.root, newkey)

    def insert_help(self, node, key):
        if key < node.key:  # if new node key < root node key
            if node.left is None:   # if no left child, new node is left child
                node.left = TreeNode(key)
                self.num_nodes += 1
            else:   # if there's a left child, new node moves down
                self.insert_help(node.left, key)
        elif key == node.key:   # duplicate nodes aren't allowed in BST
            return
        else:   # if new node key > root node key
            if node.right is None:   # if no right child, new node is right child
                node.right = TreeNode(key)
                self.num_nodes += 1
            else:   # if there's a right child, new node moves down
                self.insert_help(node.right, key)

    def find_successor(self):   # returns the node that is the inorder successor of the node
        # inorder: left subtree -> root -> right subtree
        successor = self.root.right
        while successor.left:
            successor = successor.left
        return successor

    def find_min(self): # returns min value in the tree
        current = self.root
        while current.left:   # min value in BST is the leftmost node
            current = current.left
        return current.key

    def find_max(self):
        current = self.root
        while current.right:   # max value in BST is the rightmost node
            current = current.right
        return current.key

    def inorder_print_tree(self):   # print inorder the subtree of self
        current = self.root
        return self.inorder_print_help(current)

    def inorder_print_help(self, node):
        elements = []
        if node:
            elements += self.inorder_print_help(node.left)  # append elements with all keys in left subtree
            if node.key is not None:
                elements.append(node.key)   # append elements with node key
            elements += self.inorder_print_help(node.right)  # append elements with all keys in right subtree
        return elements

    def print_levels(self): # inorder traversal prints list of pairs, [key, level of the node] where root is level 0
        current = self.root
        height = 0
        return self.print_levels_help(current, height)

    def print_levels_help(self, node, level):
        elements = []
        if node:
            elements += self.print_levels_help(node.left, level + 1) # append elements with all pairs in left subtree
            if node.key is not None:
                elements.append([node.key, level])  # append elements with key level pair
            elements += self.print_levels_help(node.right, level + 1)   # append all pairs in right subtree
        return elements

    def find(self, key):    # returns True if key is in a node of the tree, else False
        current = self.root
        return self.find_help(current, key)

    def find_help(self, node, key):
        if node.key == key:
            return True
        if key < node.key:  # key is less than node key, look at left child
            if node.left:
                return self.find_help(node.left, key)
            else:   # no left child
                return False
        if key > node.key:  # key is more than node key, look at right child
            if node.right:
                return self.find_help(node.right, key)
            else:   # no right child
                return False

    def delete(self, key):  # deletes the node containing key, assumes such a node exists
        current = self.root
        self.delete_help(current, key)  # use recursive helper function to find node and delete
        self.num_nodes -= 1  # we assume such node exists per lab specification

    def delete_help(self, node, key):
        if node is None:
            return None
        elif key < node.key: # search in left subtree
            if node.left:
                self.delete_help(node.left, key)
        elif key > node.key:    # search in right subtree
            if node.right:
                self.delete_help(node.right, key)
        else:   # the value to delete is here, key == node.key
            if node.left is None and node.right is None:    # node has no children
                node.key = None
                node = None
            elif node.left is None:   # node has only a right child
                replace = node.right
                node.key = replace.key  # replace node key with right child
                node = replace  # replace node with right child
            elif node.right is None:  # node has only a left child
                replace = node.left
                node.key = replace.key
                node = replace
            else:  # if this node has two children
                max_value_key = leftnode.find_min()
                max_value_node = leftnode.find_min_node()
                node = max_value_node
                node.key = max_value_key
                node.left = node.left.delete_help(max_value_node, max_value_key)

    def delete_child_help(self, node, key):
        pass

    def find_min_node(self): # returns node with min value, (helper for delete function)
        current = self.root
        while current.left:   # min value in BST is the leftmost node
            current = current.left
        return current

    def print_tree(self):   # print inorder the entire tree, MY COMMENT: same code as inorder_print_tree? lab confuse me
        current = self.root
        return self.inorder_print_help(current)

    def print_help(self, node):
        elements = []
        if node:
            elements += self.inorder_print_help(node.left)  # append elements with all keys in left subtree
            if node.key is not None:
                elements.append(node.key)  # append elements with node key
            elements += self.inorder_print_help(node.right)  # append elements with all keys in right subtree
        return elements

    def is_empty(self):  # returns True if tree is empty.txt, else False
        return self.num_nodes == 0