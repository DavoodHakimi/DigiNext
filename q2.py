from itertools import groupby

sample_input=["eat", "tea", "tan", "ate", "nat", "bat"]


def group_dict(dic):
    sorted_dict={}
    for key , value in dic.items():
        if value not in sorted_dict:
            sorted_dict[value] = [key]
        else:
            sorted_dict[value].append(key)

    return sorted_dict

def sort_str(string):
    out=''
    for item in sorted(string):
        out += item
    return out

def count_anagram(input:list):
    anagrams={}
    for item in input:
        anagrams[item]= sort_str(item)
    # print(anagrams)
    sorted_dict=group_dict(anagrams)
    # print(sorted_dict)
    return list(sorted_dict.values())

print(count_anagram(sample_input))