def HasPairWithSumSortedArray(input:list, sum:int)->bool:
    ilen=len(input)
    left=0
    right=ilen-1
    while left< right:
        temp_sum= input[left]+input[right] 
        if temp_sum==sum:
            return True
        elif temp_sum < sum:
            left+=1
        else:
            right-=1
    return False

input_1 = [1,2,3,9]
input_2 = [1,2,4,4]
print(HasPairWithSumSortedArray(input_1, 8))
print(HasPairWithSumSortedArray(input_2, 8))

def HasPairWithSumUnsortedArray(input:list, sum:int)->bool:
    u_set=set()
    for num in input:
        if num in u_set:
            return True
        else:
            u_set.add(sum-num)
    return False

input_1 = [1,2,3,9]
input_2 = [1,2,4,4]
input_3 = []
print(HasPairWithSumUnsortedArray(input_1, 8))
print(HasPairWithSumUnsortedArray(input_2, 8))
print(HasPairWithSumUnsortedArray(input_3, 8))
