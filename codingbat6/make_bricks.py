def make_bricks(small, big, goal):
    
    # checks to see how many large bricks you need NOT how many you have
    # lbricks = goal // 5
    
    # if lbricks > big:
    #     lbricks = big
        
    # goal = goal - (lbricks * 5)
    
    # if goal <= small:
    #     return True
    # return False
    
    if big*5 + small < goal:
        return False
    
    
    # the formula is to use all the big bricks and then use the remainder of the small bricks
    
    # we get the remainder from dividing the goal by the big bricks to get how many small bricks are left
    
    # 8 / 5 == (1 big brick 3 small bricks)
    
    # if the required is bigger than the given --> then return False
    
    # my input is (5 small bricks, 1 big bricks, 8)
    

print(make_bricks(3, 2, 10))
        






    
    
    