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

def 
