from typing import List
from unittest import TestCase, main
# j is th pointer which keep comparing and part of the for loop
# it  has to be like all the numbers before pi are less than Pivot
# all the numbers between pi and j are greater than pivot
def partition(arr:List, left, right):
    pivot = arr[right]
    pi=left-1
    for j in range(left,right):
        if arr[j] < pivot:
            pi=pi+1
            arr[pi], arr[j] = arr[j], arr[pi]
    arr[pi+1], arr[right] = arr[right], arr[pi+1]
    return pi+1


def qs(arr,l, r):
    if l>=r:
        return
    p= partition(arr, l, r)
    qs(arr, l, p-1)
    qs(arr, p+1, r )

def quicksort(arr):
    l=0
    r=len(arr)-1
    qs(arr,l,r)

class TestQuickSort(TestCase):
    def test_quicksort(self):
        a= [22,11,88,66,55,77,33,44]
        b= [7,2,1,8,6,3,5,4]
        quicksort(a)
        quicksort(b)
        # self.assertEqual(b, [1, 2, 3, 4, 6, 7, 5, 8])
        # self.assertEqual(a, [11, 22, 33, 44, 55, 77, 88, 66])
        #assert b == [1, 2, 3, 4, 6, 7, 5, 8]
        assert a == [11, 22, 33, 44, 55, 77, 88, 66]
if __name__ == '__main__':
    unittest.main()