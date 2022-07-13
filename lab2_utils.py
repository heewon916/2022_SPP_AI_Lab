# Any changes to this file will not be reflected during testing and grading
import numpy as np


class TextbookStack(object):
    """ A class that tracks the """

    def __init__(self, initial_order, initial_orientations):
        assert len(initial_order) == len(initial_orientations)
        self.num_books = len(initial_order)

        for i, a in enumerate(initial_orientations):
            # check the datas are in correct range
            assert i in initial_order
            assert a == 1 or a == 0

        self.order = np.array(initial_order)                # set the order 
        self.orientations = np.array(initial_orientations)  # set the faced up/down

    def flip_stack(self, position):
        # check if the position is over the range of num of books 
        assert position <= self.num_books

        # flip the book orders and the faced up/down 
        self.order[:position] = self.order[:position][::-1]
        self.orientations[:position] = np.abs(self.orientations[:position] - 1)[::-1]

    def check_ordered(self):
        # check all the faced up/down and the orders 
        for idx, front_matter in enumerate(self.orientations):
            if (idx != self.order[idx]) or (front_matter != 1):
                return False
        return True

    def copy(self):
        return TextbookStack(self.order, self.orientations)

    def __eq__(self, other):
        assert isinstance(other, TextbookStack), "equality comparison can only ba made with other __TextbookStacks__"
        return all(self.order == other.order) and all(self.orientations == other.orientations)

    def __str__(self):
        return f"TextbookStack:\n\torder: {self.order}\n\torientations:{self.orientations}"


def apply_sequence(stack, sequence):
    # on the given stack
    # fliping progressed 
    # following the sequence we set-up
    new_stack = stack.copy()
    for flip in sequence:
        new_stack.flip_stack(flip)
    return new_stack
