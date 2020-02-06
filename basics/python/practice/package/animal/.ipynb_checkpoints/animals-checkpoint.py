"""
Practice for python class
"""
from __future__ import absolute_import

JOBRANK = {'intern': 0, 
            'employee': 1, 
            'assistant manager': 2,
            'manager': 3,
            'general manager': 4,
            'CEO': 5}

class Animal(object):
    
    def __init__(self, name, kind='animal'):
        """
        Special method for initializing objects
        """
        # Attributes
        self.name = name
        self.__kind = kind
    
    @property
    def kind(self):
        print("Getting...")
        return self.__kind
    
    def __str__(self):
        return "__str__ method"
    
    def __repr__(self):
        return "__repr__ method"
    
        
class Cat(Animal):
    
    def __init__(self, name, kind='cat', 
                 job='intern', pay=200):
        
        # Initialize using method from parent class
        super().__init__(name, kind)
        
        try:
            self.__rank = JOBRANK[job]
        except KeyError:
            print("Job unknown: setting job into intern")
            self.__rank = JOBRANK['intern']
            
        # Private attribute: cannot access outside of the object
        self.__pay = pay
        self.__job = job
    
    def meow_job(self):
        return "Meow job is {}".format(self.__job)
    
    def meow_pay(self, rank):
        if rank > self.__rank:
            return self.__pay
        else:
            return "Meow should I told you?"
            
    @property
    def rank(self):
        return self.__rank
    
    @rank.setter
    def rank(self, new_rank):
        if new_rank < 0 or new_rank > 5:
            print("Invalid rank: needs to be 0~5.")
            return
        self.rank = new_rank