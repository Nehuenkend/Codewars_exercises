'''
PROBLEM:
A format for expressing an ordered list of integers is to use a comma separated list of either

-individual integers
-or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
'''

def arrange(x):
    if len(x) >= 3:
        return str(x[0])+'-'+str(x[-1])
        
    else:
        return ','.join([str(num) for num in x])
    
    return str(x[0])+'-'+str(x[-1])
    
def solution(args):
    output = []
    lst = []
    args += [-1234]
    for i, num in enumerate(args[1:]):
        print(i)
        lst.append(args[i])
        if args[i+1] - args[i] != 1:
            output.append(lst)
            lst = []
    output.append(lst)
    output = list(map(arrange, output))
    return ','.join(output).strip(',')
