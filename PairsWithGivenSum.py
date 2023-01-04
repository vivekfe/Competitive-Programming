

def pairs_with_given_sum(arr, sum):
    if len(arr)<=2:
        return
    count=0
    final=[]
    for i in arr:
        diff=sum-i
        if diff in arr:
            final.append([i,diff])
            count+=1
    final=set([tuple(sorted(x)) for x in final])
    return final, len(final)



if __name__ == '__main__':
    arr=[1, 5, 7, -1, 5]
    sum=6
    print(pairs_with_given_sum(arr, sum))