# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
from lab2_utils import TextbookStack

##--edit: to manage the g, h, f variables
class a_star_var():
    def __init__(self):
        self.g_cnt = 0
        self.h_cnt = 0
        self.total_f = self.g_cnt + self.h_cnt
        
    def heuristic(self, order, orientations): 
        # should check 4 conditions on the pair of stacks
        # so we should use self.order, self.orientations
        for idx, front_matter in enumerate(orientations):
            if idx%2 == 1:
                continue
            self.next = idx + 1
            if (order[idx] > order[self.next]):
                self.h_cnt += 1
            if ((order[idx] > order[self.next]) and 
                (orientations[self.next] == 1 and front_matter == 1)):
                self.h_cnt += 1
            if ((orientations[self.next],front_matter) == (0,1)
                or (orientations[self.next],front_matter) == (1,0)):
                self.h_cnt += 1
            if ((order[idx] < order[self.next])
                and (orientations[self.next],front_matter) == (0,0)):
                self.h_cnt += 1         

    # ##--edit: to calc the g_cnt; the num of the flip count 
    # def g_func(self):
    #     self.g_cnt += 1



def a_star_search(stack):
    # flip할 위치를 a* search 로 찾으려고 하는 거니까 
    # stack의 내용을 heap으로 구현한 다음에
    # 거기서 최소 f(=g+h)값을 찾는, 즉 루트 값을 찾아오면 됨
    # INPUT 
    ## TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
    # OUTPUT
    ## "a_star_search": [4]
    print(stack)
    print(stack.order)
    print(stack.orientations)
    
    flip_sequence = []
    
    tmp = a_star_var()
    tmp.heuristic(stack.order, stack.orientations)
    heappush(tmp.total_f)
    flip_point = heappop()
    flip_sequence.append(flip_point)
    stack.flip_stack(flip_point)
    
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
