from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(6))
nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]
for n in nodes:
    tree.add(Node(n))

tree.delete(9)


print('\nPrinting tree inorder:\n__________________________')
tree.inorder()
print('\nPrinting tree preorder:\n__________________________')
tree.preorder()
print('\nPrinting tree postorder:\n__________________________')
tree.postorder()
print('\nFinding a node:\n__________________________')
print(tree.find(8))
print(tree.find(9))
