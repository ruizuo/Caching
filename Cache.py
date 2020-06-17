# Cache Class
from collections import defaultdict
import datetime

class Cache:
    """
    In this class, I will provide the basic caching funtions.
    """
    
    def __init__(self):
        """
        Construct Cache Ojbect with the following variables.
        - cache: dictinary type cache, with default value {}
        - queue: Fist-in, first-out queue.
        - size: max size of the cache 
        """
        self.cache = defaultdict(set)
        self.queue = []
        self.size = 10e6
        
    def insert(self, k, v):
        """
        k presents the key,
        v is the value to be inserted.
        Insert value into cache dictionary
        """      
        if len(self.cache) < self.size:   
            # If the cache is not full, insert into cache  
            self.cache[k] = {"datetime": datetime.datetime.now(),
                            "value":v}
            
            # append this key to queue
            self.queue.append(k)       
            
        else:
            # If the cache is full, then remove the oldest one
            self.remove_redundance()
            
            # Then insert new one
            self.insert(k,v)
            
        return
    
    
    def update(self, k, v):
        """
        k presents the key,
        v is the value to be updated.
        Update the self.cache
        """

        if not self.cache[k]:
            self.delete(k)
            return "Key not found"
        else:
            self.cache[k] = {"datetime": datetime.datetime.now(),
                             "value":v}
            
            
    def delete(self, k):
        """
        k is the key to be removed
        """
        
        try:
            self.cache.pop(k)    
        except KeyError:
            print("Key not found")
            
            
    def remove_redundance():
        # get the first element from the queue
        k = self.queue.pop(0)
        
        # remove the element from cache by key
        
        self.delete(k)
        
        return       
            
    @property
    def size(self):
        """
        Return the length of the cache
        """
        return len(self.cache)
    
    
        
            

        