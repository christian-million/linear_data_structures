from LinearData import LinearData


class Queue(LinearData):
    '''First In First Out data structure where pushes happen on the left and pops on the right
    Inherits from `LinearData` and only overrides the `append` method, since appending should happen on the left.
    '''
    def __init__(self, *args, unpack=True):
        super().__init__(*args, unpack=True)
        self.delimiter = ' ~> '

    def append(self, item):
        '''In a Queue, items are appended to the start / left'''
        super().append(item, right=False)


class CarmenQ(Queue):
    '''Extension of the Queue class with method to find where in the Queue "Carmen Sandiego" is.'''
    def __init__(self, *args, unpack=True):
        super().__init__(*args, unpack=True)

    def find_carmen(self, name="Carmen SanDiego"):
        '''Returns the smallest index of the Node that contains `name` or None if it is not found
        Arguments
        ---------
        name -- the object whose index you want to find
        '''

        # Assume the worst - Carmen is nowhere to be found
        i = None

        # If at least 1 node exists
        if self.head:

            # Initialize a reference to overwrite
            current_node = self.head

            # Capture the length of the Q
            n = 0

            # Loop through each node
            while current_node:
                n += 1

                # If a match is found, overwrite i with the newest find
                if current_node.data == name:
                    i = n-1

                # Skip along to the next
                current_node = current_node.nxt

            # We found i from the left, but I'm assuming the line "starts" at the right.
            if i:
                i = n - i

        if i:
            print(f"{name} in index {i}.")

        else:
            print(f"Could not find {name} in queue")

        return i


if __name__ == "__main__":

    print("Testing empty stack")
    tst_queue = Queue()
    print(tst_queue)

    print("Pushing some items")
    tst_queue.append(1)
    print(tst_queue)
    tst_queue.append(2)
    print(tst_queue)
    tst_queue.append(3)
    print(tst_queue)

    print("Popping some items")
    for i in range(3):
        print(tst_queue)
        print(tst_queue.pop())

    print("Pushing some items")
    tst_queue.append(1)
    print(tst_queue)
    tst_queue.append(2)
    print(tst_queue)
    tst_queue.append(3)
    print(tst_queue)

    print("Testing contains...")
    print(f"test_queue.contains(1): {tst_queue.contains(1)}")
    print(f"test_queue.contains(5): {tst_queue.contains(5)}")

    print("Testing New Queue")
    new_queue = Queue([1, 2, 3, 4, 5, 6, 7])
    print(new_queue)

    print("Testing CarmenQ")
    c_q = CarmenQ([1, 2, 3, "Carmen SanDiego", 5])
    print(c_q)
    print(c_q.find_carmen())
