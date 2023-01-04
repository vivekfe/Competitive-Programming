from collections import Counter
def char_count(sample):
    l={}
    for i in sample:
        l[i]= 1 if l.get(i) is None else l[i]+1
    return l

def non_repeat(sample):
    f=char_count(sample)
    for i in sample:
        if f.get(i)==1:
            return i


if __name__ == '__main__':
    sample= "algorithm"
    print(non_repeat(sample))