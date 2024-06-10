class Singleton():
    _instances = {}

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        
        return cls._instances[cls]
    

