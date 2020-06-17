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
        
    
        
        