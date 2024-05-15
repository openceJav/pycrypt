'''Singleton Pattern Decorator

This module provides a decorator that can be used when creating Singleton classes.

Example:
    from decorators.singleton import singleton

    @singleton
    class SingletonClass():
        def __init__(self):
            pass

    s_in = SingletonClass()
    
    
Attributes:
    _instances (dict): A dictionary to store the instances of the Singleton classes.
    
Todo:
    * Add tests and test cases to ensure the decorator works as expected.
    * Add more functionality to the decorator to handle more complex Singleton classes.
    * Iterate over code and ensure code quality and consistency.
    * Document changes and updates to this decorator in the CHANGELOG.md file (automated eventually).
    
@Author: Muhammad Bilal Khan
@Date: 2025-05-14
@Version: 1.0.0
@Since: 1.0.0
'''

def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
            
    return get_instance