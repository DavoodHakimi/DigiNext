
# sample_input=[100,102,103,104,105, 4, 200, 1, 3, 2,101,50,51,49]
sample_input= [100, 4, 200, 1, 3, 2]

def find_longest(numbers:list):
    threads=[]
    numbers=sorted(numbers)
    for number in numbers[:len(numbers)-1]:

        if number - 1 not in numbers:
            current_num = number
            current_sequence = [current_num]

            while current_num + 1 in numbers:
                current_num += 1
                current_sequence.append(current_num)

            threads.append(current_sequence)

    longest=sorted(threads,key=len,reverse=True)[0]
    print(longest)

find_longest(sample_input)
