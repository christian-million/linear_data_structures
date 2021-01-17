class Node:
    '''A single element of stack'''
    def __init__(self, data, nxt=None):
        # The actual content of the Node
        self.data = data

        # This should be a reference to the subsequent Node or None
        self.nxt = nxt

    def __str__(self):
        # Return the data string representation
        return str(self.data)


class Queue:
    '''First In First Out data structure where pushes happen on the left and pops on the right'''
    def __init__(self):
        self.head = None

    def push(self, data):
        '''Adds element to the top of the stack'''
        if self.head:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data)

    def pop(self):
        '''Removes and returns the right-most element'''
        if self.head:
            prev_node = self.head
            current_node = self.head

            while current_node:
                if current_node.nxt:
                    prev_node = current_node
                    current_node = current_node.nxt
                else:
                    prev_node.nxt = None
                    return current_node.data
        else:
            return None

    def contains(self, item):
        '''Check to see if the LinkedList contains an element'''
        if self.head:
            current_node = self.head
            while current_node:

                # Confirmed this works for None
                if current_node.data == item:
                    return True
                else:
                    current_node = current_node.nxt

            return False

        else:
            return False

    def reverse(self):
        '''Reverses the order of the Stack'''
        if self.head:

            previous_node = self.head
            next_node = self.head.nxt
            previous_node.nxt = None

            while next_node.nxt:
                # We need something to reference the unreversed
                tether = next_node.nxt

                # We can override this because we reference it above
                next_node.nxt = previous_node

                # Establish new previous node
                previous_node = next_node

                # Our original tether to the unreversed acts as our next node
                next_node = tether

            # replace the None pointer with the reversed
            next_node.nxt = previous_node

            # Make the last node the new head.
            self.head = next_node

    def __str__(self):
        if self.head is None:
            return "None"
        else:
            current_node = self.head
            out = str(self.head.data)

            while current_node.nxt:
                current_node = current_node.nxt

                out += f' ~> {current_node.data}'

            return out


if __name__ == "__main__":

    print("Testing empty stack")
    tst_queue = Queue()
    print(tst_queue)

    print("Pushing some items")
    tst_queue.push(1)
    print(tst_queue)
    tst_queue.push(2)
    print(tst_queue)
    tst_queue.push(3)
    print(tst_queue)

    print("Popping some items")
    for i in range(3):
        print(tst_queue)
        print(tst_queue.pop())

    print("Pushing some items")
    tst_queue.push(1)
    print(tst_queue)
    tst_queue.push(2)
    print(tst_queue)
    tst_queue.push(3)
    print(tst_queue)

    print("Testing contains...")
    print(f"test_queue.contains(1): {tst_queue.contains(1)}")
    print(f"test_queue.contains(5): {tst_queue.contains(5)}")
