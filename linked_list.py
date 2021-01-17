# Resources
# https://towardsdatascience.com/how-to-loop-through-your-own-objects-in-python-1609c81e11ff
# https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
# https://docs.python.org/3/reference/datamodel.html#object.__contains__
import copy


class Node:
    '''A single element of a linked list'''
    def __init__(self, data, nxt=None):
        # The actual content of the Node
        self.data = data

        # This should be a reference to the subsequent Node or None
        self.nxt = nxt

    def __str__(self):

        # Return the data string representation
        return str(self.data)


class LinkedListIter:
    '''A LinkedList Iterator Class'''
    def __init__(self, LinkedList):
        self.LinkedList = LinkedList

        # initialize the first node to be the head
        self.i_node = self.LinkedList.head

    def __next__(self):
        if self.i_node:
            out = self.i_node.data
            self.i_node = self.i_node.nxt
            return out

        else:
            raise StopIteration


class LinkedList:
    '''Linked list contains nodes which reference subsequent nodes'''
    def __init__(self):
        self.head = None

    def append_right(self, data):
        '''Add a node to the left end of the LinkedList'''
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head

            while current_node.nxt:
                current_node = current_node.nxt

            current_node.nxt = Node(data)

    def append_left(self, data):
        '''Add a node to the right end of the LinkedList'''
        if self.head:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data)

    def pop_right(self):
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

    def pop_left(self):
        '''Removes and returns the left-most element'''
        if self.head:
            out = self.head.data
            self.head = self.head.nxt
            return out
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

    def __contains__(self, item):
        '''Allows for use with `in` operator'''
        return self.contains(item)

    def copy(self):
        return copy.deepcopy(self)

    def __add__(self, other):
        og = copy.deepcopy(self)

        if isinstance(other, (LinkedList, Node)):

            other_copy = copy.deepcopy(other.head)

            if og.head is None:
                og.head = other_copy
            else:
                current_node = og.head

                while current_node.nxt:
                    current_node = current_node.nxt

                current_node.nxt = other_copy
        else:
            og.append_right(other)

        return og

    def __iter__(self):
        '''Allows the LinkedList to become an iterable. Calls LinkedListIter'''
        return LinkedListIter(self)

    def __len__(self):
        '''Counts the number of nodes in the LinkedList
        Added bonus of considering empty LinkedList as Falsey
        '''
        if self.head is None:
            return 0
        else:
            i = 1
            current_node = self.head

            while current_node.nxt:
                i += 1
                current_node = current_node.nxt

            return i

    def __str__(self):
        if self.head is None:
            return "None"

        else:
            current_node = self.head
            out = str(self.head.data)

            while current_node.nxt:
                current_node = current_node.nxt

                out += f' -> {current_node.data}'

            return out


if __name__ == '__main__':

    # Test that Node works and prints appropriately
    tst_node = Node(1)

    print(tst_node)

    # Test logical value
    print(f"{True if tst_node else False}")

    print("Testing LinkedList with no parameters")
    tst_list = LinkedList()
    print(tst_list)

    print("Equality check for LinkedList with no parameters")
    print(f"{True if tst_list else False}")

    print("Append Right...")
    tst_list.append_right(1)
    print(tst_list)

    tst_list.append_right(2)
    print(tst_list)

    tst_list.append_right(3)
    print(tst_list)

    print("Append Left...")
    tst_list.append_left(10)
    print(tst_list)

    print("Pop Right...")
    p_right = tst_list.pop_right()
    print(f"Popped Value: {p_right}")
    print(f"New Linked List: {tst_list}")

    print("Append Right...")
    tst_list.append_right(3)
    print(tst_list)

    print("Pop Left...")
    p_left = tst_list.pop_left()
    print(f"Popped Value: {p_left}")
    print(f"New Linked List: {tst_list}")

    print("Testing Iteration...")
    for node1 in tst_list:
        for node2 in tst_list:
            print(node1, node2)

    print("Testing contains...")
    tst_value = 3
    print(f"tst_list: {tst_list}")
    print(f"tst_list.contains({tst_value}): {tst_list.contains(tst_value)}")

    print("Testing contains...")
    tst_value = None
    print(f"tst_list: {tst_list}")
    print(f"tst_list.contains({tst_value}): {tst_list.contains(tst_value)}")

    print("Append Right...")
    tst_list.append_right(None)
    print(tst_list)

    print("Testing contains...")
    print(f"tst_list: {tst_list}")
    print(f"tst_list.contains({tst_value}): {tst_list.contains(tst_value)}")

    print("Append Right...")
    tst_list.append_right(['a', 'b', 'c'])
    print(tst_list)

    print("Testing contains...")
    tst_value = ['b', 'a', 'c']
    print(f"tst_list: {tst_list}")
    print(f"tst_list.contains({tst_value}): {tst_list.contains(tst_value)}")

    print("Testing `in` operator use...")
    tst_value = ['a', 'b', 'c', 'd']
    print(f"tst_list: {tst_list}")
    print(f"{tst_value} in tst_list: {tst_value in tst_list}")

    print("Testing __add__...")
    tst_list2 = LinkedList()
    tst_list2.append_right('a')
    tst_list2.append_right('b')
    tst_list2.append_right('c')

    print(f"tst_list: {tst_list}")
    print(f"tst_list2: {tst_list2}")

    tst_list + tst_list2
    print("tst_list + tst_list2")
    print(f"{tst_list}")

    print("tst_list + 5")
    tst_list + 5
    print(f"{tst_list}")

    print("new_tst_list = tst_list + tst_list2")
    new_tst_list = tst_list + tst_list2
    print(f"{new_tst_list}")

    print("new_tst_list = new_tst_list + 5")
    new_tst_list = new_tst_list + 5
    print(f"{new_tst_list}")

    print(f"new_tst_list: {new_tst_list}")
    print(f"len(new_tst_list): {len(new_tst_list)}")
