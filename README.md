## Goals:

- Write classes for each these including the following methods:

    - Stack

        - append

        - pop

        - contains (takes a single argument returns True if it's in the Stack and False if not.)

    - Queue

        - append

        - pop

        - contains

    - Linked List

        - append_left

        - append_right

        - pop_left

        - pop_right

        - contains

    - Doubly Linked List

        - append_left

        - append_right

        - pop_left

        - pop_right

        - contains

- You may use the collections library's double ended queue (deque) as a starting point for stacks and Queues, but you should alias the methods appropriately. This is also lame.

- You should write the linked lists by hand. Hint, they should NOT contain a List.

# TODO

- [ ] Create a Doubly Linked List

- [ ] Create a LinearDataStructure class that the rest of these can inherit from

    - This will reduce code duplication for some of the cool methods like reverse and `__contains__`.

- [ ] Go over everything with comments

- [ ] Find a more scalable way to test these

- [ ] Easier way to initialize each structure:

    - `__init__(*args, unpack=False)` where `unpack=True` will convert an `*args` of length 1 `and` type list/dict/tuple as collection of nodes?