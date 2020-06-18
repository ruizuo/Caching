# Case 1: If k is allowed to be negative

from collections import defaultdict

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if not nums: 
            return 0
        
        count = 0
        dic = defaultdict(int)
        dic_com = defaultdict(bool)
        res = []
        
        for ele in nums:
            dic[ele] += 1            
        
        for key in list(dic):
            if k > 0:
                if dic[key-k] > 0:
                    key_new = str(key-k) + "-" + str(key)
                    
                    if not dic_com[key_new]:
                        dic_com[key_new] = True
                        res.append((key-k, key))
                        count += 1
            elif k < 0:
                if dic[key-k] > 0:
                    key_new = str(key) + "-" + str(key-k)
                    
                    if not dic_com[key_new]:
                        dic_com[key_new] = True
                        res.append((key,key-k))
                        count += 1
            else:
                if dic[key] > 1:
                    key_new = str(key) + "-" + str(key)
                    
                    if not dic_com[key_new]:
                        dic_com[key_new] = True
                        res.append((key,key))
                        count += 1   
         
        print(res)
        return count 


nums = [1,3,5]
k = 2

solution = Solution()
result = solution.countPairs(nums, k)
print(result)




