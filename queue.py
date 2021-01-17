from LinearData import LinearData


class Queue(LinearData):
    '''First In First Out data structure where pushes happen on the left and pops on the right'''
    def __init__(self):
        super().__init__()
        self.delimiter = ' ~> '

    def append(self, item):
        '''In a Queue, items are appended to the start / left'''
        super().append(item, right=False)


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
