import math
import unittest
def second_smallest(arr):
    pleft, pright= math.inf, math.inf
    for i in range(len(arr)):
        if arr[i]<=pleft:
            pright=pleft
            pleft = arr[i]
        elif arr[i]<pright and arr[i]!=pright:
            pright=arr[i]
    return pright


arr= [100,2,5,3,119,1,90]
class NoTestSecondSmallest(unittest.TestCase):
    def test_second_smallest(self):
        self.assertEqual(second_smallest(arr), 2)

if __name__=='__main__':
    unittest.main()
