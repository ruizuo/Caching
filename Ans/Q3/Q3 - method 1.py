# Method 1

from collections import defaultdict

class DSU:
    def __init__(self):
        self.p = list(range(10001))
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution(object):
    def Merge(self, data):
        """
        :type data: List[tuple]
        :rtype: list[list]
        """
        
        if not data: 
            return []
        
        dsu = DSU()
        
        name_to_id = {}
        phone_to_id = {}
        email_to_id = {}
        
        res = []
        
        index = 0
        
        for name, phone, email in data:
            if name not in name_to_id:
                name_to_id[name] = index
            else:
                dsu.union(index, name_to_id[name])
                
            if phone not in phone_to_id:
                phone_to_id[phone] = index
            else:
                dsu.union(index, phone_to_id[phone])
                
            if email not in email_to_id:
                email_to_id[email] = index
            else:
                dsu.union(index, email_to_id[email])
            
            index += 1
        
        ans = defaultdict(list)
        
        for idx, val in enumerate(data):
            ans[dsu.find(idx)].append(idx)
        
        #print(dsu.p)
        
        for key, value in ans.items():
            res.append(value)
        
        return res
        


# In[3]:


data = [("username1","phone_number1", "email1"),
        ("username2","phone_number2", "email2"),
        ("username3","phone_number3", "email3"),
        ("username4","phone_number1", "email4"),
        ("username2","phone_number5", "email4"),
        ("username1","phone_number6", "email6")]

solution = Solution()
result = solution.Merge(data)
print(result)