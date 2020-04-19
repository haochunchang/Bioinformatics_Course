class ListNode(object):

    def __init__(self, value):
        self.value = value
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
