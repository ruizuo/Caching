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
            # Remove the empty {} 
            del self.cache[k]
            return "Key not found"
        else:
            # Update the value by key
            self.cache[k] = {"datetime": datetime.datetime.now(),
                             "value":v}
            
            # update the value in queue
            try 
                # remove the element from the queue by value
                self.queue.remove(k)  
                
                # Append the key to the queue
                self.queue.append(k)          
                
            except ValueError:
                # Exception if key not be found in queue
                print("Oops!  That was no valid vlaue.")        
                 
        return    
            
    def delete(self, k):
        """
        k is the key to be removed
        """      
        try:           
            # remove the element from the queue by value
            self.queue.remove(k)                
            # reomve key from cache
            self.cache.pop(k)    
        except KeyError:
            # exception if key not found
            print("Key not found")
        except ValueError:
            # Exception if key not be found in queue
            print("Oops!  That was no valid vlaue.")          
            
    def remove_redundance():
        """
        Remove the first element (the key to be removed from cache) from the queue, 
        if the cache is full.
        """
        # get the first element from the queue
        k = self.queue.pop(0)
        
        # remove the element from cache by key 
        try:
            self.cache.pop(k)    
        except KeyError:
            print("Key not found")
        
        return       
    
    
        
            

        