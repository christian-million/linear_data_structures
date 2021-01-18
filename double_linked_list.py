from LinearData import LinearData, Node


class DblNode(Node):
    '''DblNode references the previous node AND the next node'''
    def __init__(self, data, nxt=None, prev=None):
        super().__init__(data, nxt)
        self.prev = prev


class DblLinkedList(LinearData):
    '''LinkedList where each node references the previous and subsequent nodes'''
    def __init__(self, *args, unpack=True):
        self.head = None

        # args is technically a tuple, so not using any lists :)
        if args:
            # Unpack each element of single list or tuple into individual nodes
            if len(args) == 1 and isinstance(args[0], (list, tuple)) and unpack:
                args = args[0]

            for arg in args:
                self.append(arg)

        # Set a default delimiter
        self.delimiter = ' <-> '

    def append(self, data, right=True):
        '''Add a node to the end of the DblLinkedList object'''
        if self.head:
            if right:
                # Initialize a current_node to overwrite
                current_node = self.head

                # Swipe through each node until the last
                while current_node.nxt:
                    current_node = current_node.nxt

                # Add the new node to the end
                current_node.nxt = DblNode(data, prev=current_node)

            # On left append, new node becomes the head
            else:
                self.head = DblNode(data, self.head)
        # On empty list, new node becomes the head
        else:
            self.head = DblNode(data)

    def pop(self, right=True):
        '''Removes and returns the the right/left element'''
        if self.head:
            if right:

                # Initialize reference nodes to overwrite
                current_node = self.head

                while current_node:

                    # skip to the end
                    if current_node.nxt:
                        current_node = current_node.nxt

                    else:
                        # Remove references to the last item
                        current_node.prev.nxt = None

                        # Return it's data
                        return current_node.data

            # On left pop, the heads next becomes the head
            else:
                # capture the data before overwriting
                out = self.head.data

                # Replace the head before returning
                self.head = self.head.nxt

                # Remove reference to old head
                self.head.prev = None

                # Return the popped data
                return out

    def append_left(self, item):
        '''Appended item to the start / left
        Arguments
        ---------
        item -- element to append'''
        self.append(item, right=False)

    def append_right(self, item):
        '''Appended item to the end / right
        Arguments
        ---------
        item -- element to append
        '''
        self.append(item)

    def pop_left(self):
        '''Removes and returns the the left most element'''
        return self.pop(right=False)

    def pop_right(self):
        '''Removes and returns the the right most element'''
        return self.pop()

    def reverse(self):
        '''Reverses the order of the structure'''
        if self.head:

            # Initialize some reference variables to overwrite
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
