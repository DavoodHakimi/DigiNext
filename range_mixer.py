import numpy as np

smaple_input=[(10,8),(6,2),(3,1)]


def check_overlap(r1,r2):
    l1=list(range(r1[1],r1[0]))
    l2=list(range(r2[1],r2[0]))
    if len(np.intersect1d(l1,l2)) == 0:
        return False
    else:
        return True
    
def range_mixer(range_list:list):
    
    new_ranges=[]
    while len(range_list) != 0:
        a=0
        current_range=range_list[0]
        range_list.pop(0)
        for item in range_list:
            if check_overlap(current_range,item) == True:
                new_range=(max(item[0],current_range[0]),min(current_range[1],item[1]))
                new_ranges.append(new_range)
                range_list.pop(range_list.index(item))
                a+=1
        if a == 0 :
            new_ranges.append(current_range)
    print(new_ranges)


range_mixer(smaple_input)  