from LinearData import LinearData


class Stack(LinearData):
    '''Last In First Out data structure where pops and pushes only happen at one end.'''
    def __init__(self, *args, unpack=True):
        super().__init__(*args, unpack=True)
        self.delimiter = ' / '

    def append(self, item):
        '''In a Stack, items are appended to the top / left'''
        super().append(item, right=False)

    def pop(self):
        '''In a Stack, items are popped from the top / left'''
        return super().pop(right=False)


if __name__ == "__main__":

    print("Testing empty stack")
    tst_stack = Stack()
    print(tst_stack)

    print("Pushing some items")
    tst_stack.append(1)
    print(tst_stack)
    tst_stack.append(2)
    print(tst_stack)
    tst_stack.append(3)
    print(tst_stack)

    print("Popping some items")
    for i in range(3):
        print(tst_stack.pop())

    print("Pushing some items")
    tst_stack.append(1)
    print(tst_stack)
    tst_stack.append(2)
    print(tst_stack)
    tst_stack.append(3)
    print(tst_stack)
    tst_stack.append(4)
    print(tst_stack)
    tst_stack.append(5)
    print(tst_stack)

    print("Testing contains...")
    print(f"tst_stack.contains(1): {tst_stack.contains(1)}")
    print(f"tst_stack.contains(5): {tst_stack.contains(5)}")

    print("Testing reverse...")
    print(f"Current stack:{tst_stack}")
    print("...reversing...")
    tst_stack.reverse()
    print(f"Now: {tst_stack}")

    new_stack = Stack([1, 2, 3, 4, 5, 6, 8])
    print(new_stack)
