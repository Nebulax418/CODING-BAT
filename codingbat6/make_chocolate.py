# def make_chocolate(small, big, goal):
    
#     # get the remaining amount of small bricks
    
#     # these two added up should be the goal
#     big_cal = big * 5
#     small_bricks = 5 % big_cal
    
#     # check if you can only use small bricks or only big bricks first
    
    
    
#     if small_bricks >= small:
#         return small_bricks
    
#     if small_bricks <= small:
#         if small_bricks == 0:
#             return 0
#         else:
#             return small_bricks if (big_cal + small_bricks) == goal else -1 
    
# correct solution
def make_chocolate(small, big, goal):
    
    # get small needed first
    
    small_needed = goal - (big * 5)
    
    # is it even enough to make the goal?
    if goal > big * 5 + small:
        return -1
    
    # if the small bars needed is less than or equal to how many we have
    # and also if it a positive real number greater than or equal to 0
    if small_needed <= small and small_needed >= 0:
        return small_needed
    
    # if the number of large bars are overshooting the goal
    if small_needed < 0 and small_needed <= small:
        return small_needed
        
    return -1
    
        
    

print(make_chocolate(4, 1, 9))
    
    
    