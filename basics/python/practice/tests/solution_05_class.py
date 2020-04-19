from animals import *
  
tom = Cat(name='tom', job='CEO', pay=1e8)
garfield = Cat(name='garfield', job='employee', pay=500)

# Problem 1: Promote garfield to general manager
garfield.rank = 4

# Problem 2: (Modify animals.py) 
# Garfield wants more salary, please add a setter to modify pay.
"""
@pay.setter
def pay(self, new_pay):
    if new_pay < 0:
        print("Invalid pay: needs to be > 0.")
        return
    self.__pay = new_pay
"""

# Problem 3: Convert the inputs to ListNode such that
# 1 -> 2 -> 3 -> 4, where '->' means .next
class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

inputs = [1, 2, 3, 4]

root = ListNode(inputs[0])
current = root
for value in inputs[1:]:
    node = ListNode(value)
    current.next = node
    current = node

node = root
output = ""
while node.next != None:
    output += "{} -> ".format(node.value)
    node = node.next
output += "{}".format(node.value)
print(output)
