import numpy as np
import random

sample_input=[[1, 3, 5], [7, 8, 10], [12, 15, 18]]
Goal=8


def search_goal(numbers,goal):

    vals=np.array(numbers).flatten() #converting matrix into a 1d array
    num = 0
    
    while num != goal:
        guess = random.randint(0,len(vals)-1)
        print("Original list",vals)
        gess=vals[guess]
        if gess == goal:
            print("found it!!",gess)
            break
        else:
            if gess < goal:
                vals=vals[guess:]
            else:
                vals=vals[:guess]
        
        print("edited list:",vals)
        print("guess:",gess)
        print("goal:",goal)
        print("----------------------------------")

search_goal(sample_input,Goal)