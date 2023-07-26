class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Define array of differences 
        diff = []
        for i in range(len(nums)):

          #Allocate prefix and suffix and delete duplicates with set
          prefix = [*set(nums[0:i+1])]
          sufix = [*set(nums[i+1:len(nums)])]

          #Allocate the amount of repeated elements in prefix and sufix
          repeatedElementsInPrefix = (i+1) - len(prefix)
          repeatedElementsInSufix = (len(nums)-(i+1)) - len(sufix)

          #Update sizes of prefix and sufix subarrays without repeated elements and substract 
          diff.append((i+1-repeatedElementsInPrefix)-(len(nums)-(i+1)-repeatedElementsInSufix))
        return diff