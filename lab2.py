# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop


def a_star_search(stack):
    # flip할 위치를 a* search 로 찾으려고 하는 거니까 
    # stack의 내용을 heap으로 구현한 다음에
    # 거기서 최소 f(=g+h)값을 찾는, 즉 루트 값을 찾아오면 됨
    # INPUT 
    ## TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
    # OUTPUT
    ## "a_star_search": [4]
    flip_sequence = []
    
    
    # --- v ADD YOUR CODE HERE v --- #
    # for matter in stack.order:
    #     heappush(matter)
    #     stack.
    # where we will flip; the sequence
    return flip_sequence

    # ---------------------------- #


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
