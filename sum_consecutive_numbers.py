# find the number of ways a natural number can be represented as the sum of
# two or more consecutive numbers

def num_consecutive_sum(num):
    counter = 0
    L=1
    final_list=[]
    while (L*(L+1)<2*num):
       a=(num-L*(L+1)/2)/(L+1)
       if a-int(a)==0.0:
           counter=counter+1
           seq= [int(a+i) for i in range(L+1)]
           final_list.append(seq)
       L+=1
    return counter, final_list

num=100
y,z=num_consecutive_sum(num)
print(f'{num} can be represented as the sum of consequetive numbers in {y} ways')
print(z)
