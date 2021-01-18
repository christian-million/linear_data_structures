from LinearData import LinearData, Node


class DblNode(Node):
    '''DblNode references the previous node AND the next node'''
    def __init__(self, data, nxt=None, prev=None):
        super().__init__(data, nxt)
        self.prev = prev


class DblLinkedList(LinearData):
    '''LinkedList where each node references the previous and subsequent nodes'''
    def __init__(self):
        super().__init__()
        self.delimiter = ' <-> '

    def append(self, data, right=True):
        '''Add a node to the end of the DblLinkedList object'''
        if self.head:
            if right:
                current_node = self.head

                while current_node.nxt:
                    current_node = current_node.nxt

                current_node.nxt = DblNode(data, prev=current_node)

            else:
                self.head = DblNode(data, self.head)
        else:
            self.head = DblNode(data)

    def pop(self, right=True):
        '''Removes and returns the the right/left element'''
        if self.head:
            if right:

                current_node = self.head

                while current_node:
                    if current_node.nxt:
                        current_node = current_node.nxt
                    else:
                        current_node.prev.nxt = None
                        return current_node.data
            else:
                out = self.head.data
                self.head = self.head.nxt
                self.head.prev = None
                return out

    def append_left(self, item):
        '''Appended item to the start / left'''
        self.append(item, right=False)

    def append_right(self, item):
        '''Appended item to the end / right'''
        self.append(item)

    def pop_left(self):
        '''Removes and returns the the left most element'''
        return self.pop(right=False)

    def pop_right(self):
        '''Removes and returns the the right most element'''
        return self.pop()

    def reverse(self):
        '''Reverses the order of the LinearData'''
        if self.head:

            previous_node = self.head
            next_node = self.head.nxt
            previous_node.nxt = None

            while next_node.nxt:
                # We need something to reference the unreversed
                tether = next_node.nxt

                # We can override this because we reference it above
                next_node.nxt = previous_node
                next_node.prev = tether

                # Establish new previous node
                previous_node = next_node

                # Our original tether to the unreversed acts as our next node
                next_node = tether

            # replace the None pointer with the reversed
            next_node.nxt = previous_node

            # Make the last node the new head.
            self.head = next_node
            self.head.prev = None


if __name__ == '__main__':

    print("Testing DblLinkedList")
    tst_dbl = DblLinkedList()
    print(tst_dbl)

    print("Testing Append Right...")
    for i in range(3):
        tst_dbl.append(i)
        print(tst_dbl)

    print("Testing Pop Right...")
    for i in range(1, 2):
        tst_dbl.pop()
        print(tst_dbl)

    print("Testing Append Left...")
    for i in range(1, 3):
        tst_dbl.append(i, right=False)
        print(tst_dbl)

    print("Testing Pop Left...")
    for i in range(1, 2):
        tst_dbl.pop(right=False)
        print(tst_dbl)

    print("Testing Append Left...")
    for i in range(1, 3):
        tst_dbl.append(i, right=False)
        print(tst_dbl)

    print("Testing Reverse...")
    tst_dbl.reverse()
    print(tst_dbl)

    print("Testing Re-Reverse...")
    tst_dbl.reverse()
    print(tst_dbl)
