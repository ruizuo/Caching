# Cache Class
from collections import defaultdict

class Cache:
    """
    In this class, I will provide the basic caching funtions.
    """
    
    def __init__(self):
        """
        Construct Cache Ojbect with the following variables.
        - cache
        - size 
        """
        self.cache = defaultdict(set)
        self.size = 10e6
        
    def insert(self, k, v):
        """
        k present the key,
        v is the value to be inserted.
        Insert value into cache dictionary
        """
        
        self.cache[k] = v
        
        return
    
    
    def update(self, k, v):
        """
        k present the key,
        v is the value to be updated.
        Update the self.cache
        """
        if not self.cache[k]:
            return "Not exists"
        else:
            self.cache[k] = v
            
            

        