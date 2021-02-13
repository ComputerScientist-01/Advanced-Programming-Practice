class ques1:

   def __init__(self):
       pass

   def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i

arr = [int(x) for x in input().split()]   
target = int(input())  
obj = ques1()
index1,index2 = obj.twoSum(arr, target)     
print (index1 + 1)
print (index2 + 1)  
#print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
